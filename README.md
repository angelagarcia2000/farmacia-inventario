# Sistema de Gestión para Farmacia El Descuento

## Información del Proyecto
* **Asignatura:** Ingeniería de Software
* **Periodo Lectivo:** 2026-2026
* **Líder de Grupo:** María Angela García Toro
* **Módulo a Implementar:** Control de Inventario y Medicamentos
* **Requerimientos SRS:** RF-01 (Registrar medicamentos) y RF-06 (Consultar/buscar medicamentos)
* **Stack Tecnológico:** Python + Django (con MySQL)

---

## Flujo de Trabajo con Ramas (GitHub Flow)

Para mantener la calidad y estabilidad del código fuente, el equipo utilizará el flujo **GitHub Flow**:

1. **`main` (Rama Principal):** Contiene código estable y probado listo para producción. No se realizan commits directos sobre esta rama.
2. **`feature/*` (Ramas de Trabajo):** Cada nueva funcionalidad o corrección se desarrolla en una rama independiente creada a partir de `main`.
   * *Ejemplo:* `feature/registrar-medicamento`, `feature/buscar-medicamento`.
3. **Commits Claros:** Cada cambio se guarda con mensajes descriptivos en presente indicativo (ej. `git commit -m "Agrega validación para la fecha de vencimiento"`).
4. **Pull Requests (PR):** Para fusionar el código de una rama `feature/*` a `main`, se abre un Pull Request en GitHub, el cual es revisado y requiere que la canalización de Integración Continua (CI) se ejecute exitosamente (check verde ✔).