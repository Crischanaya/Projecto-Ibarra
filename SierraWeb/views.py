from django.shortcuts import render, redirect
from django.http import HttpRequest,JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest
from SierraWeb.models import Usuarios, Paquetes, Compras
from datetime import datetime
import sys, json
import re





# Create your views here.

def barrancas(request):
    if 'user' in request.session:
      current_user = request.session['user']
      param = {'Usuario':current_user}
      return render(request, "SierraWeb/barrancas.html",param)

    return render(request, "SierraWeb/barrancas.html")

def contacto(request):
    if 'user' in request.session:
       current_user = request.session['user']
       param = {'Usuario':current_user}
       return render(request, "SierraWeb/contacto.html",param)

    if request.method=="POST":
       
        subject=request.POST["asunto"] 

        if request.POST["contacto"] == "telefono":
            contactar = "telefono"
        else:
            contactar = "correo"      

        message= "Nombre: "+ request.POST["nombre"]  +"\nMensaje:"+ request.POST["mensaje"] + "\nCorreo: " + request.POST["correo"] + "\nTeléfono: " + request.POST["telefono"] + "\nContactar: " + contactar + "\nFecha a Contactar: " + request.POST["fecha"] + "\nHora a Contactar: " + request.POST["hora"]

        email_from=settings.EMAIL_HOST_USER

        recipient_list=["agenciasierratours@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

    return render(request, "SierraWeb/contacto.html")



def creel(request):
    if 'user' in request.session:
      current_user = request.session['user']
      param = {'Usuario':current_user}
      return render(request, "SierraWeb/creel.html",param)

    return render(request, "SierraWeb/creel.html")

def huapoca(request):
    if 'user' in request.session:
       current_user = request.session['user']
       param = {'Usuario':current_user}
       return render(request, "SierraWeb/huapoca.html",param)

    return render(request, "SierraWeb/huapoca.html")

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'Usuario': current_user}
        status = request.GET.get('status')
        if status == "completed" or status == "error":
            return render(request,'SierraWeb/index.html',{"alerta": status,'Usuario': current_user})
        return render(request,'SierraWeb/index.html',param)
    else:
        return redirect('index')    

def index(request):
    if 'user' in request.session:
       current_user = request.session['user']
       param = {'Usuario':current_user}
       return render(request, "SierraWeb/index.html",param) 

    return render(request, 'SierraWeb/index.html')    

def login(request):  #Ya verifica si el correo del usuario existe
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['pass']
        if Usuarios.objects.filter(correo=correo).count() == 0:
            return redirect('login')
        else:
            check_user = Usuarios.objects.get(correo=correo, password=password)
            if check_user:
                usuario = check_user.nombre_usuario 
                request.session['user'] = usuario
                return redirect('home')

    return render(request, "SierraWeb/login.html")

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('index')    

def nosotros(request):
    if 'user' in request.session:
      current_user = request.session['user']
      param = {'Usuario':current_user}
      return render(request, "SierraWeb/nosotros.html",param)

    return render(request, "SierraWeb/nosotros.html")  
    
def recowata(request):
    if 'user' in request.session:
      current_user = request.session['user']
      param = {'Usuario':current_user}
      return render(request, "SierraWeb/recowata.html",param)
    
    return render(request, "SierraWeb/recowata.html")

def registro(request):
    return render(request, "SierraWeb/registro.html")

def pasarela(request):
    if 'user' in request.session:
        #paquete= Paquetes.objects(id_Paquete_contains=paquetes)
        idpaquete=request.GET['1']
        request.session['id_paquete'] = idpaquete
        ruta='SierraWeb/img/pasarela/pas'+idpaquete+'.jpg'
        paquete=str(Paquetes.objects.get(id_paquete=idpaquete))
        idpaquete=int(request.GET['1'])
        nombrepaquete=paquete[2:200]
        precioo= Paquetes.objects.filter(id_paquete=idpaquete).values
    
        if(idpaquete <4):
            
            lugar="Huapoca"
        else:
            if(idpaquete <7):
                lugar="Creel"
            else:
                lugar="Barrancas del Cobre"

        return render(request, "SierraWeb/pasarela.html",{"nombre_paquete":nombrepaquete, "lugar":lugar, "ruta":ruta,"precioo":precioo})        
    else:
        alerta = {'alerta':"activar"}
        return render(request, "SierraWeb/login.html",alerta)  
        

def pago(request):
    paquete_id= request.session['id_paquete']
    paquete = Paquetes.objects.get(pk=paquete_id)
    current_user = request.session['user']
    usuario = Usuarios.objects.get(nombre_usuario=current_user)
    data = json.loads(request.body)
    personas = data['personas']
    order_id = data['orderID']
    detalle = GetOrder().get_order(order_id)
    detalle_precio = float(detalle.result.purchase_units[0].amount.value)
    total_personas = int(personas)
    for i in range(total_personas):
        total= (float(paquete.precio))*(i*.20)
        acum_total= total + float(paquete.precio)
    x = datetime.now()

    #print(acum_total)    
    #print(detalle_precio)
    #print(paquete.precio)

    if detalle_precio == acum_total:
        transaccion = CaptureOrder().capture_order(order_id,debug=True)
        print(transaccion.result)
        print("entro a guardar")
        pedido=Compras(
            id_compra=transaccion.result.id,
            nombre_usuario= usuario.nombre_usuario,
            apellido_usuario=usuario.apellido,
            nombre_paypal=transaccion.result.payer.name.given_name,
            apellido_paypal=transaccion.result.payer.name.surname,
            correo_cliente=transaccion.result.payer.email_address,
            paquete=Paquetes.objects.get(pk=paquete_id),
            n_personas=personas,
            fecha_paquete=x.strftime("%d/%m/%Y"),
            status=transaccion.result.status,
            codigo_estado=transaccion.status_code,
            total_de_compra=transaccion.result.purchase_units[0].payments.captures[0].amount.value
        )
        pedido.save()

        data = {
            "id": f"{transaccion.result.id}",
            "nombre_cliente": f"{transaccion.result.payer.name.given_name}",
            "mensaje": "completed"
        }

        return JsonResponse(data)
        #return render(request,"SierraWeb/index.html",{"pago_finalizado":"completed"})
    else:
        data={
            "mensaje": "Error"
        }   
        return JsonResponse(data)
    


def add_registro(request):
    #print("ENTRO AL GUARDADO")
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    correo = request.POST["correo"]
    password = request.POST["password"]
    if Usuarios.objects.filter(correo=correo).count()>0:
        return redirect('registro')
    else:
        usuarios = Usuarios(nombre_usuario=nombre,apellido=apellido,correo=correo,password=password)
        usuarios.save()
        if usuarios !=None:
            respuesta = "completed"
        else:
            respuesta = "error"
        return render(request, "SierraWeb/registro.html",{"respuesta":respuesta})        
        #return redirect('login')
    #if usuarios != None:
    #    respuesta = "completed"
    #    print(usuarios)
    #else:
    #    respuesta = "error"

    #return render(request, "SierraWeb/registro.html",{"respuesta":respuesta})   


 # INTEGRACION DE PAYPAL
class PayPalClient:
    def __init__(self):
        self.client_id = "ASfsijiN0GpuI7nV8DQFNOKGDt966uv3MZx_U8J8gRSyLn2b51SpBHgFetuFmCVfmYTVffgDUxTi4QBX"
        self.client_secret = "EINXILPWJqa4CHykfAPncbmSe6kz6NtgHmquYZHdkwOG_do8e9w0j-1MN8MEtPxXE960pu54UYQ20OpC"

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = iter(json_data.__dict__.items())
        else:
            itr = list(json_data.__dict__.items())
        for key,value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                        self.object_to_json(value) if not self.is_primittive(value) else\
                         value
        return result
    def array_to_json_array(self, json_array):
        result =[]
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if  not self.is_primittive(item) \
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, str) or isinstance(data, int)



#Obtener los detalles de la transaccion
class GetOrder(PayPalClient):

  #2. Set up your server to receive a call from the client
  """You can use this function to retrieve an order by passing order ID as an argument"""   
  def get_order(self, order_id):
    """Method to get order"""
    request = OrdersGetRequest(order_id)
    #3. Call PayPal to get the transaction
    response = self.client.execute(request)
    return response
    #4. Save the transaction in your database. Implement logic to save transaction to your database for future reference.
   # print('Status Code: ', response.status_code)
   # print('Status: ', response.result.status)
   # print('Order ID: ', response.result.id)
   # print('Intent: ', response.result.intent)
   # print('Links:')
   # for link in response.result.links:
   #   print(('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method)))
   # print('Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
    #                   response.result.purchase_units[0].amount.value))
#if __name__ == '__main__':
#  GetOrder().get_order('REPLACE-WITH-VALID-ORDER-ID')



class CaptureOrder(PayPalClient):

  #2. Set up your server to receive a call from the client
  """this sample function performs payment capture on the order.
  Approved order ID should be passed as an argument to this function"""

  def capture_order(self, order_id, debug=False):
    """Method to capture order using order_id"""
    request = OrdersCaptureRequest(order_id)
    #3. Call PayPal to capture an order
    response = self.client.execute(request)
    #4. Save the capture ID to your database. Implement logic to save capture to your database for future reference.
    if debug:
      print ('Status Code: ', response.status_code)
      print ('Status: ', response.result.status)
      print ('Order ID: ', response.result.id)
      print ('Links: ')
      for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
      print ('Capture Ids: ')
      for purchase_unit in response.result.purchase_units:
        for capture in purchase_unit.payments.captures:
          print ('\t', capture.id)
      print ("Buyer:")
  #    print "\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
  #      response.result.payer.name.given_name + " " + response.result.payer.name.surname,
  #      response.result.payer.phone.phone_number.national_number)
    return response



#if __name__ == "__main__":
#  order_id = 'REPLACE-WITH-APPORVED-ORDER-ID'
#  CaptureOrder().capture_order(order_id, debug=True)