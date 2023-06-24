$.validator.addMethod("terminaPor",function(value, element, parametro){
    if(value.endsWith(parametro)){
        return true;
    }
    return false;

}, "debe terminar por {0}")

$("#formulario_contacto").validate({
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
        tipo_solicitud: {
            required: true,
            minlength: 5,
            maxlenght: 200
        }
    }
})
 $("#guardar").click(function () {
    if($("#formulario_contacto").valid() == false) {
        return;
    }
    let nombre =$("#nombre").val()
    let email =$("#email").val()
    let tipoSolicitud =$("#tipo_solicitud").val()
    let aviso =$("#avisos").is(":chacked")
})