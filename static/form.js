const form = document.getElementById('form');
const inputs = document.querySelectorAll('#form input');

const expresiones = {
	username: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	password: /^.{4,12}$/, // 4 a 12 digitos.
	email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
}

const validarFormulario = (e) => {
	switch (e.target.name) {
		case "username":
      if (expresiones.username.test(e.target.value)) {
          document.querySelector('#username-input .form__input-error').classList.remove('form__input-error-activo');
          campos[username] = true;
      }
      else{
          document.querySelector('#username-input .form__input-error').classList.add('form__input-error-activo');
          campos[username] = false;
      }
		break;
		case "email":
      if (expresiones.email.test(e.target.value)) {
          document.querySelector('#email-input .form__input-error').classList.remove('form__input-error-activo');
          campos[username] = true;
      }
      else{
          document.querySelector('#email-input .form__input-error').classList.add('form__input-error-activo');
          campos[username] = false;
      }
		break;
		case "password":
      if (expresiones.password.test(e.target.value)) {
          document.querySelector('#password-input .form__input-error').classList.remove('form__input-error-activo');
          campos[username] = true;
      }
      else{
          document.querySelector('#password-input .form__input-error').classList.add('form__input-error-activo');
          campos[username] = false;
      }
		break;
	}
}

inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});
