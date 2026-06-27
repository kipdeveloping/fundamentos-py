<div align="center">
  <h1>🐍 Python Fundamentals Pack</h1>
  <p><strong>El paquete de iniciación definitivo para dominar las bases de Python</strong></p>
  
  <p>
    <img src="https://img.shields.io/badge/version-1.0.0-blue.svg?style=flat-square" alt="Version">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python Version">
    <img src="https://img.shields.io/badge/license-MIT-green.svg?style=flat-square" alt="License">
    <img src="https://img.shields.io/badge/status-active-success.svg?style=flat-square" alt="Status">
  </p>
</div>

---

Aprende, experimenta y domina los fundamentos de Python con este archivo interactivo y de referencia rápida. `fundamentos.py` está diseñado para ser tu "hoja de trucos" (cheat sheet) personal, cubriendo todo desde variables hasta estructuras de datos complejas.

## ✨ Características (Features)

*   **📘 Sintaxis Clara:** Ejemplos directos al grano, sin código innecesario.
*   **🛠️ Interactivo:** Comenta y descomenta bloques usando `"""` para probar funcionalidades por separado.
*   **🎮 Minijuegos Integrados:** Aprende lógica con un mini-juego de *Piedra, Papel o Tijera*.
*   **📚 Estructuras de Datos:** Incluye listas, tuplas y diccionarios complejos (con datos anidados).

---

## 🚀 Uso rápido (Quick Start)

Ejecutar el entorno de pruebas es extremadamente sencillo. 

1. Asegúrate de tener Python instalado en tu máquina.
2. Abre tu terminal favorita en el directorio del archivo.
3. Ejecuta el script principal:

```bash
python fundamentos.py
```

> **Tip de Pro:** Ve al código fuente de `fundamentos.py` y quita las comillas triples (`"""`) de la sección que quieras ver funcionando en la consola. ¡El código está pensado para que lo modifiques y lo rompas!

---

## 📖 Tabla de Contenidos del Código

Este archivo aborda los siguientes temas paso a paso de forma estructurada:

| Tema | Descripción | Conceptos Clave |
| :--- | :--- | :--- |
| **1. Variables** | Creación y salida de datos. | `print`, *f-strings* |
| **2. Operadores Matemáticos** | Cálculos aritméticos básicos. | `+`, `-`, `*`, `/` |
| **3. Operadores Relacionales** | Comparaciones lógicas para condicionales. | `>`, `<`, `==`, `!=` |
| **4. Condicionales** | Toma de decisiones. | `if`, `elif`, `else`, Anidados |
| **5. Operadores Lógicos** | Combinación de múltiples condiciones. | `and`, `or` |
| **6. Estructuras de Datos** | Colecciones de múltiples valores. | `list`, `tuple`, `dict` |
| **7. Bucles** | Iteración de elementos y repeticiones. | `for`, `in`, `range()` |

---

## 💻 Ejemplos de Código (Code Snippets)

### Trabajando con Estructuras de Datos Anidadas
```python
name_dict = {
    'name': 'jose', 
    'favorite_foods': ["pizza", "hamburguesa"],
    'address': {
        'city': "Lima",
        'country': "Peru"
    }
}
print(name_dict["address"]["city"]) # Salida: Lima
```

### Lógica Condicional (Piedra, Papel, Tijera)
```python
if sel_pl1 == "Piedra" and sel_pl2 == "Tijera":
    print(f"{player1} gano la ronda")
# ... más lógica manejada elegantemente con elif
```

---

## 📝 Notas de Versión (Release Notes)

### 1.0.0
* Lanzamiento inicial.
* Se agregó soporte para estructuras de datos y bucles básicos.
* Se incluyó el algoritmo de *Piedra, Papel o Tijera*.

---

## 🐛 Problemas Conocidos (Known Issues)

*   Por defecto, la mayoría de los `print` están silenciados para no inundar la terminal de texto. Recuerda descomentarlos según el bloque específico que estés estudiando.

---

**¡Disfruta programando!** Si este archivo te ha servido de apoyo, compártelo con la comunidad. 💜
