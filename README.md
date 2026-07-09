# ⚡ TaskFlow — Sistema de Gestión de Tareas

> Proyecto de Laboratorio — Desarrollo de Software  
> Aplicación web desarrollada con **Django** para la gestión de tareas y proyectos por equipo.

---

## 📸 Capturas de Pantalla

| Login | Dashboard |
|---|---|
| ![Login](https://raw.githubusercontent.com/Jose28221/laboratorioTaskDS/main/docs/login.png) | ![Dashboard](https://raw.githubusercontent.com/Jose28221/laboratorioTaskDS/main/docs/dashboard.png) |

---

## 🚀 Características

- 🔐 **Autenticación** — Login y logout con el sistema de autenticación de Django
- 📋 **Dashboard personal** — Cada usuario ve sus tareas asignadas
- ✅ **Gestión de tareas** — Crear, completar y desmarcar tareas
- 📁 **Gestión de proyectos** — Organizar tareas por proyecto
- 👑 **Roles de usuario** — Administradores pueden crear proyectos y asignar tareas
- 🎨 **Diseño premium** — Dark mode con glassmorphism y animaciones

---

## 🛠️ Tecnologías

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.x | Lenguaje base |
| Django | 6.x | Framework web |
| SQLite | — | Base de datos (desarrollo) |
| HTML/CSS | — | Templates con diseño dark mode |

---

## 📁 Estructura del Proyecto

```
laboratorioTaskDS/
│
├── manage.py                    # Utilidad de gestión de Django
│
├── taskflow/                    # Configuración del proyecto
│   ├── settings.py              # Configuración global
│   ├── urls.py                  # Rutas principales
│   ├── wsgi.py
│   └── asgi.py
│
└── tareas/                      # App principal
    ├── models.py                # Modelos: Proyecto, Tarea
    ├── views.py                 # Vistas: dashboard, crear, completar
    ├── forms.py                 # Formularios: TareaForm, ProyectoForm
    ├── admin.py                 # Registro en el panel admin
    ├── migrations/              # Migraciones de base de datos
    └── templates/
        ├── base.html            # Template base (navbar, estilos)
        ├── dashboard.html       # Panel principal
        ├── crear_proyecto.html  # Formulario de proyecto
        ├── crear_tarea.html     # Formulario de tarea
        └── registration/
            └── login.html       # Página de inicio de sesión
```

---

## ⚙️ Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Jose28221/laboratorioTaskDS.git
cd laboratorioTaskDS
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install django
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor

```bash
python manage.py runserver
```

Abre tu navegador en: **http://127.0.0.1:8000**

---

## 🗺️ Rutas de la Aplicación

| URL | Vista | Descripción |
|---|---|---|
| `/` | `dashboard` | Panel principal (requiere login) |
| `/login/` | `LoginView` | Página de inicio de sesión |
| `/logout/` | `LogoutView` | Cerrar sesión |
| `/proyectos/nuevo/` | `crear_proyecto` | Crear nuevo proyecto (admin) |
| `/tareas/nueva/` | `crear_tarea` | Crear nueva tarea (admin) |
| `/tareas/<id>/completar/` | `completar_tarea` | Marcar/desmarcar como completada |
| `/admin/` | Admin Django | Panel de administración |

---

## 🗄️ Modelos de Datos

### `Proyecto`
| Campo | Tipo | Descripción |
|---|---|---|
| `nombre` | CharField(100) | Nombre del proyecto |
| `descripcion` | TextField | Descripción (opcional) |
| `fecha_creacion` | DateTimeField | Fecha de creación (automática) |

### `Tarea`
| Campo | Tipo | Descripción |
|---|---|---|
| `titulo` | CharField(200) | Título de la tarea |
| `descripcion` | TextField | Descripción (opcional) |
| `completada` | BooleanField | Estado (default: False) |
| `proyecto` | ForeignKey → Proyecto | Proyecto al que pertenece |
| `asignada_a` | ForeignKey → User | Usuario responsable |

---

## 👥 Roles de Usuario

| Rol | Crear Proyectos | Crear Tareas | Ver Tareas propias | Completar Tareas |
|---|:---:|:---:|:---:|:---:|
| **Superusuario / Admin** | ✅ | ✅ | ✅ | ✅ |
| **Usuario normal** | ❌ | ❌ | ✅ | ✅ |

---

## 🧑‍💻 Autor

**Jose28221** — Desarrollo de Software

---

## 📄 Licencia

Este proyecto fue desarrollado como laboratorio académico.
