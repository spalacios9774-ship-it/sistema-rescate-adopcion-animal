# Sistema de Control de Rescate y Adopción Animal

Diseño UML y patrones de diseño para un sistema que permite registrar y gestionar casos de rescate,
atención veterinaria y adopción de animales.

Actividad 1 – Desarrollo de Sistemas Informáticos, Universidad Técnica de Manabí.

## Patrones de diseño
| Patrón | Dónde se aplica |
|---|---|
| Singleton | `GestorCasos` (una única instancia coordina los casos) |
| Observer | `PublicadorEventos`, `NotificadorVoluntarios`, `TableroRefugio` |
| Factory Method | `AnimalFactory` y las fábricas por especie (expedientes) |
| MVC | `CasoControlador`, `CasoVista` y los modelos |

## Ramas (Gitflow)
`main` y `master` (estables), `develop` (integración), `feature/casos-rescate` y `feature/notificaciones`.

## Estructura
```
diagramas/        diagramas UML
documentacion/    informe de diseño (PDF)
src/              código: modelos, servicios, controladores y vistas
```

## Ejecutar (Python 3.8 o superior)
```bash
python src/main.py
```
