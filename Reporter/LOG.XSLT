<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
 <html>
 <Head>
        <style type="text/css">

          body {
          background:#fff;
          margin:0;
          padding:40px 20px;
          font-family: "Arial", Arial, Sans-serif;
          font-size: 16px;
          color:#000;
          }

          table {
          margin:5px 5px 0;
          border:0px solid #222;
          font-size: 0.8em;
          }

          td {
          margin:5px 5px 0;
          padding:10px 10px 10px 10px;
          vertical-align:text-top;
          border:1px solid #222;
          border-width:1px 1px 1px 1px;
          }

          td.light {
          border:0px solid #222;
          }

          td.number {
          text-align:right;
          }

          td.status {
          text-align:right;
          vertical-align:text-bottom;
          }

        </style>


 </Head>
 <body>
   <!--OVER RESULT -->
   <xsl:variable name="OVER_STATUS" select="REPORT/OVER_STATUS"/>
   <xsl:variable name="STATUS" select="REPORT/LOG_ENTRY/STATUS"/>



   <h2>自动化测试执行报告</h2>
   <!--table -->
   <table border="1">
     <!--all result value-->
     <tr bgcolor="white" height = "35">
        <td>Overall Test Result</td>
        <td><xsl:value-of select="$OVER_STATUS"/></td>
        <td colspan="2"> </td>
     </tr>

     <tr bgcolor="#D8BFD8" height = "35">
       <th>执行时间</th>
       <th>单步结果</th>
       <th>响应CODE</th>
       <th>Response信息</th>
     </tr>



       <!--select font color -->
       <xsl:variable name="fontColor">
           <xsl:choose>
               <xsl:when test="$STATUS = FAILED or $STATUS = PASSED">
                   <xsl:text>white</xsl:text>
               </xsl:when>
               <xsl:otherwise>black</xsl:otherwise>
           </xsl:choose>
       </xsl:variable>

       <!--background color-->
       <xsl:variable name="backgroundColor">
           <xsl:choose>
               <xsl:when test="$STATUS = 'FAILED'">
                   <xsl:text>rgb(255,0,0)</xsl:text>
               </xsl:when>
               <xsl:when test="$STATUS = 'PASSED'">
                   <xsl:text>rgb(60,179,113)</xsl:text>
               </xsl:when>
               <xsl:otherwise>
                   <xsl:text>white</xsl:text>
               </xsl:otherwise>
           </xsl:choose>
       </xsl:variable>

       <!--log entry-->
       <xsl:for-each select = "REPORT/LOG_ENTRY">


           <tr>
               <td><xsl:value-of select="EXECUTION_TIME"/></td>
               <td bgcolor="{$backgroundColor}"><xsl:value-of select="STEP_RESULT"/></td>
               <td><xsl:value-of select="COMPONENT_NAME"/></td>
               <td><xsl:value-of select="STEP_DESCRIPTION"/></td>
           </tr>
       </xsl:for-each>

       <tr bgcolor="white">
           <font color="{$fontColor}">
               <td colspan="4">Overall Test Result:<xsl:value-of select="$OVER_STATUS"/></td>
           </font>
       </tr>
   </table>
 </body>
 </html>
</xsl:template>
</xsl:stylesheet>