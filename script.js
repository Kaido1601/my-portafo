document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const inputs = form.querySelectorAll("input");
  
    // Función para validar cada campo en tiempo real
    inputs.forEach(input => {
      input.addEventListener("input", () => {
        if (input.checkValidity()) {
          input.style.border = "2px solid limegreen";
        } else {
          input.style.border = "2px solid red";
        }
      });
    });
  
    // Al enviar el formulario
    form.addEventListener("submit", (e) => {
      e.preventDefault(); // Evita que se envíe automáticamente
  
      let todoValido = true;
      inputs.forEach(input => {
        if (!input.checkValidity()) {
          input.style.border = "2px solid red";
          todoValido = false;
        }
      });
  
      if (todoValido) {
        alert("Formulario enviado con éxito 🎉");
        form.reset(); // Limpia el formulario
        inputs.forEach(input => input.style.border = "none"); // Limpia bordes
      } else {
        alert("Por favor, completa todos los campos correctamente.");
      }
    });
  });
  