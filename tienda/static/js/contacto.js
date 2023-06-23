var input = document.getElementsByClassName('formulario__input'); 


for(var i = 0; i < input.length; i++){
    input[i].addEventListener('keyup', function(){
        if(this.value.length>=1){
            this.nextElementSibling.classList.add('fijar')
        }else{
            this.nextElementSibling.classList.remove('fijar')

        }
    })
}
$.validator.addMethod("terminaPor",function(value, element, parametro){
    if(value.endsWith(parametro)){
        return true;
    }
    return false;

}, "debe terminar por {0}")

$("#formu").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlenght: 30
        },
        email: {
            required: true,
            email: true,
            terminaPor: "gmail.com"

        },
        telefono: {
            required: true,
            number: true,
            min: 1,
            max: 10
        }
    }
})
 $("#guardar").click(function () {
    if($("#formu").valid() == false) {
        return;
    }
    let nombre =$("#nombre").val()
    let email =$("#email").val()
    let telefono =$("#telefono").val()
})

