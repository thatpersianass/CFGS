<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Factura <xsl:value-of select="factura/numero"/></title>
        <style>
          body { font-family: Arial, sans-serif; margin: 40px; }
          table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
          th, td { border: 1px solid black; padding: 8px; vertical-align: top; }
          th { background-color: #f0f0f0; }
          .right { text-align: right; }
          .center { text-align: center; }
          .no-border td { border: none; }
          .titulo { font-weight: bold; text-align: center; }
          .subtitulo { font-weight: bold; }
        </style>
      </head>

      <body>

        <!-- Cabecera principal -->
        <table>
          <tr>
            <td class="titulo" colspan="4">
              Factura: <xsl:value-of select="factura/numero"/>
            </td>
          </tr>
          <tr>
            <th>FACTURA</th>
            <td><xsl:value-of select="factura/numero"/></td>
            <th>FECHA</th>
            <td><xsl:value-of select="factura/fecha"/></td>
          </tr>
        </table>

        <!-- Emisor y Receptor -->
        <table>
          <tr>
            <th colspan="2" class="center">EMISOR</th>
          </tr>
          <tr>
            <th>CIF</th>
            <td><xsl:value-of select="factura/emisor/cif"/></td>
          </tr>
          <tr>
            <th>Nombre</th>
            <td><xsl:value-of select="factura/emisor/nombre"/></td>
          </tr>
        </table>

        <table>
          <tr>
            <th colspan="2" class="center">RECEPTOR</th>
          </tr>
          <tr>
            <th>CIF</th>
            <td><xsl:value-of select="factura/receptor/cif"/></td>
          </tr>
          <tr>
            <th>Nombre</th>
            <td><xsl:value-of select="factura/receptor/nombre"/></td>
          </tr>
        </table>

        <!-- Detalle de conceptos -->
        <table>
          <tr>
            <th colspan="4" class="center">DETALLE</th>
          </tr>
          <tr>
            <th>Concepto</th>
            <th class="center">Unidades</th>
            <th class="right">Precio</th>
            <th class="right">Subtotal</th>
          </tr>
          <xsl:for-each select="factura/detalle/item">
            <tr>
              <td><xsl:value-of select="concepto"/></td>
              <td class="center"><xsl:value-of select="unidades"/></td>
              <td class="right"><xsl:value-of select="precio"/>€</td>
              <td class="right"><xsl:value-of select="subtotal"/>€</td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- Totales -->
        <table>
          <tr>
            <td colspan="3" class="right"><strong>NETO</strong></td>
            <td class="right"><xsl:value-of select="factura/neto"/>€</td>
          </tr>
          <tr>
            <td colspan="3" class="right"><strong>IGIC <xsl:value-of select="factura/igic/@porcentaje"/>%</strong></td>
            <td class="right"><xsl:value-of select="factura/igic"/>€</td>
          </tr>
          <tr>
            <td colspan="3" class="right"><strong>TOTAL</strong></td>
            <td class="right"><xsl:value-of select="factura/total"/>€</td>
          </tr>
        </table>

        <!-- Transferencia -->
        <table class="no-border">
          <tr>
            <td class="subtitulo">Transferencia a IBAN:</td>
            <td><xsl:value-of select="factura/iban"/></td>
          </tr>
        </table>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
