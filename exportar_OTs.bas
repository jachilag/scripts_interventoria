Attribute VB_Name = "exportar_OTs"
'este script sirve para generar un archivo de tipo texto que relaciona los casos de siniestros con su respectivas OT,
'para luego ser procesado con un script de python para diferentes usos entre ellos separar los pdf's de los protocolos y bitacora
Sub Archivo_OTs()

Dim T_SINIESTROS As Object
Set T_SINIESTROS = ThisWorkbook.Sheets("Siniestros").ListObjects("T_SINIESTROS")
filas = T_SINIESTROS.Range.Rows.Count
colum = T_SINIESTROS.Range.Columns.Count

datos = seleccionar(2, "seleccione carpeta donde desea guardar el archivo")
myFile = datos(0, 0) & "\datosOTs.txt"  'nombre del archivo de salida
Open myFile For Output As #1    'crea y abre un archivo de salida
quincena = ThisWorkbook.Sheets("INFORME").Range("quincena").Value

'----ciclo que coloca primero el dato del caso del siniestro y despues la OT asociada
For i = 2 To filas
        With T_SINIESTROS
            If quincena = .Range(i, Range("T_SINIESTROS[[#Headers],[Quincena]]").Column).Value Then
                Print #1, .Range(i, Range("T_SINIESTROS[[#Headers],[Nº]]").Column).Value & "," & .Range(i, Range("T_SINIESTROS[[#Headers],[O.T No]]").Column).Value _
                & "," & .Range(i, Range("T_SINIESTROS[[#Headers],[NOMBRE ARCHIVO]]").Column).Value
            End If
        End With
Next i
Close #1
MsgBox "Archivo Generado"
End Sub
