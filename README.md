## Particionamiento de Palíndromos

<p>El Archivo <code>main.py</code> Contiene el codigo principal encargado de medir los tiempos de los algorimos.</p>
<p>El Archivo <code>Algoritmo_A.py</code> Contiene el codigo del algoritmo de complejidad O(n³)</p>
<p>El Archivo <code>Algoritmo_B.py</code> Contiene el codigo del algoritmo de complejidad O(n²)</p>
<p>El Archivo <code>palabras-aleatorias.py</code> contiene un programa simple que genera palabras aleatorias, al ejecutarse pide el numero de palabras a generar, viene configurado por defecto para generar palabras de largo maximo 500 caracteres</p>
<p>La Carpeta <code>datos y resultados utilizados</code> Contiene los archivos generados utilizados y los resultados obtenidos junto con el archivo .xlsx con los graficos</p>

### Ejecución
Para usar este codigo, clonar el repositorio y ejecutar

```console
python main.py
```
Debe existir dentro del directorio del proyecto un archivo <code>palabras.txt</code> con las palabras generadas por el programa <code>palabras-aleatorias.py</code>

El código generará un archivo .csv que puede ser abierto en un software de hojas de calculo para generar un gráfico, se genera una tabla con las siguientes columnas
<ul>
  <li>Palabra</li>
  <li>Largo de la palabra</li>
  <li>Tiempo del Algoritmo A</li>
  <li>Tiempo del Algoritmo B</li>
</ul> 
