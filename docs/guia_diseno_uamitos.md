# 🎨 Guía de Diseño para la App — Secundaria UAMITOS

Este documento contiene la configuración de estilo oficial de la aplicación, incluyendo la paleta de colores institucional, tipografía recomendada y cómo integrarla en PySide6 con soporte para tema claro/oscuro y cambios dinámicos.

---

## 🎨 Paleta de Colores UAMITOS

| Nombre             | Hex       | Uso recomendado                          |
| ------------------ | --------- | ---------------------------------------- |
| Rojo institucional | `#B71C1C` | Color principal (títulos, botones clave) |
| Gris oscuro        | `#848484` | Fondo de sidebar, texto secundario       |
| Gris claro         | `#E0E0E0` | Bordes, separadores, hover sutil         |
| Blanco             | `#FFFFFF` | Fondo principal                          |
| Gris muy claro     | `#FAFAFA` | Alternativa de fondo para claridad       |
| Negro              | `#000000` | Texto principal en tema claro            |

---

## 🔤 Tipografía: Inter

- Tipo: Sans-serif moderna, legible y responsiva
- Sitio oficial: [https://rsms.me/inter/](https://rsms.me/inter/)
- Licencia: Open Source (gratis para uso personal y comercial)

### 📁 Integración en el proyecto

1. **Descarga** la fuente `Inter-Regular.ttf`
2. **Colócala** en una carpeta dentro del proyecto:

```
/RGV-UAMITOS-App
│
├── fuentes/
│   └── Inter-Regular.ttf
├── main.py
├── estilos.qss
```

3. **Carga desde Python** con `QFontDatabase`:

```python
from PySide6.QtGui import QFontDatabase, QFont

# Cargar fuente desde archivo
font_id = QFontDatabase.addApplicationFont("fuentes/Inter-Regular.ttf")
if font_id != -1:
    family = QFontDatabase.applicationFontFamilies(font_id)[0]
    app.setFont(QFont(family))
else:
    print("⚠️ No se pudo cargar la fuente Inter")
```

---

## 🎨 Aplicación de estilos con QSS

En tu archivo `estilos.qss`:

```css
* {
  font-family: "Inter";
  font-size: 14px;
  color: #000000;
  background-color: #fafafa;
}
```

---

## 🌗 Soporte para Tema Claro y Oscuro (Bonus)

### 1. Crea dos archivos `.qss`:

**`estilo_claro.qss`**

```css
* {
  font-family: "Inter";
  background-color: #fafafa;
  color: #000000;
}
```

**`estilo_oscuro.qss`**

```css
* {
  font-family: "Inter";
  background-color: #2c2c2c;
  color: #ffffff;
}
```

### 2. Carga dinámica desde Python:

```python
def aplicar_estilo(path_qss: str):
    with open(path_qss, "r") as f:
        estilo = f.read()
        app.setStyleSheet(estilo)
```

Y en tu código:

```python
modo_oscuro = True  # cambia esto según el botón o toggle

if modo_oscuro:
    aplicar_estilo("estilo_oscuro.qss")
else:
    aplicar_estilo("estilo_claro.qss")
```

---

> Desarrollado por **RGV Innovations** · Proyecto final de PVOE · UAM Azcapotzalco
