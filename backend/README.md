# 📚 Catálogo Backend - Django REST + OAuth2

Este proyecto corresponde al **backend** de una aplicación web full-stack para el manejo de catálogos de **Libros y Autores**, desarrollado con **Django** y **Django REST Framework**, exponiendo únicamente una **API REST protegida con OAuth 2.0**.

El backend no renderiza vistas HTML, su función principal es proveer servicios REST para ser consumidos por un frontend en React.

---

## 🎯 Objetivo del Proyecto

Desarrollar una API REST que permita:

- Gestionar autores.
- Gestionar libros relacionados a un autor (relación uno a muchos).
- Implementar autenticación segura mediante OAuth 2.0.
- Proveer un CRUD completo usando métodos HTTP.

---

## 🛠️ Tecnologías Usadas

- Python  
- Django  
- Django REST Framework  
- Django OAuth Toolkit  
- SQLite (por defecto)  
- CORS Headers  

---

## 📂 Estructura del Proyecto

- `catalogo/` → App principal
- `models.py` → Definición de Autor y Libro
- `serializers.py` → Serialización de datos
- `views.py` → ViewSets API
- `urls.py` → Rutas REST
- `settings.py` → Configuración OAuth y DRF

---

## 🔗 Endpoints Principales

| Método | Endpoint        | Descripción             |
|--------|----------------|------------------------|
GET      | `/api/autores/` | Listar autores         |
POST     | `/api/autores/` | Crear autor            |
PUT      | `/api/autores/{id}/` | Actualizar autor |
DELETE   | `/api/autores/{id}/` | Eliminar autor   |
GET      | `/api/libros/`  | Listar libros          |
POST     | `/api/libros/`  | Crear libro            |
PUT      | `/api/libros/{id}/` | Actualizar libro |
DELETE   | `/api/libros/{id}/` | Eliminar libro   |

---

## 🔐 Autenticación OAuth 2.0

La API está protegida con OAuth 2.0 usando **django-oauth-toolkit**.

Flujo general:

1. Obtener token desde el backend.
2. Enviar el token en el header:

```http
Authorization: Bearer TU_TOKEN
