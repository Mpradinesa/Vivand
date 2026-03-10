# Vivand - Gestión de Cuidados Integrales 🩺

Sistema de gestión de turnos y ficha clínica digital diseñado para servicios de cuidados a domicilio y pequeñas empresas de salud, adaptable a veterinarias, servicios esteticos u otros servicios que requieran agenda. Este MVP permite de ejemplo, se permite coordinar pacientes, cuidadores y servicios de manera eficiente, ademas de mensajes instantaneos de confirmacion o cancelacion de cita vía WhatsApp.

## 🚀 Características principales

* **Dashboard Estadístico:** Visualización de ingresos mensuales y servicios realizados.
* **Gestión de Turnos:** Agenda interactiva con visualización de calendario.
* **Notificaciones Automáticas:** Confirmación de turnos vía **WhatsApp** mediante la API de **UltraMsg**.
* **Reportes en Excel:** Generación de Fichas Médicas por paciente y reportes de pagos para cuidadores.
* **Arquitectura:** Backend robusto desarrollado con **Django** y base de datos **PostgreSQL**.
* **Interfaz Moderna:** Diseño profesional enfocado en la experiencia de usuario (Mobile First).

## 🛠️ Tecnologías utilizadas

* **Backend:** Python 3.x, Django 5.x
* **Base de Datos:** PostgreSQL
* **Mensajería:** API de UltraMsg (Integración vía `requests`)
* **Reportes:** Openpyxl
* **Frontend:** HTML5, CSS (Tailwind/Bootstrap), JavaScript (FullCalendar)

## 📦 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/vivand.git](https://github.com/tu-usuario/vivand.git)
   cd vivand