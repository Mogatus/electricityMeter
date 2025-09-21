from main import extract_today_wh_values

TEST_STR = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "DTD/xhtml1-transitional.dtd">
<html><head>
<html>
<head>
<title> EDM (EMS Direct Manager) -V1.0   Samsung SDI @ 2015</title>

<style type="text/css">
td {
  font-amily: Arial;
  font-size: 11px;
  background-color: #FFFFFF;
  vertical-align: middle;
  border: thin solid #333333;
}

.stblue {
  font-amily: Arial;
  font-size: 11px;
  background-color: #99CCFF;
  border: thin solid #000080;
  padding: 1px;
  margin: 1px;
  vertical-align: middle;
}

.stred {
  font-family: Arial;
  font-size: 11px;
  background-color: #FFCCCC;
  border: thin solid #993300;
  padding: 1px;
  margin: 1px;
  vertical-align: middle;
}
.title_gray {
  font-family: Arial;
  font-size: 12px;
  background-color: #CCCCCC;
  border: thin dashed #333333;
  padding: 1px;
  margin: 1px;
  vertical-align: middle;
  font-weight: bold;
}
.st_gray {
  font-family: Arial;
  font-size: 11px;
  background-color: #CCCCCC;
  border: thin solid #000080;
  padding: 1px;
  margin: 1px;
  vertical-align: middle;
}
.styellow {
  font-family: Arial;
  font-size: 11px;
  background-color: #FFFF66;
  border: thin solid #663300;
  padding: 1px;
  margin: 1px;
  vertical-align: middle;
}
.stgreen {
  font-family: Arial;
  font-size: 11px;
  background-color: #CCFF33;
  border: thin solid #333300;
  padding: 1px;
  margin: 1px;
  vertical-align: middle;
}
.stpurple {
  font-family: Arial;
  font-size: 11px;
  background-color: #CC99FF;
  border: thin solid #660066;
  padding: 1px;
  margin: 1px;
  vertical-align: middle;
}
.font_bold_red {
  font-weight: bold;
  color: #FFCCCC;
  background-color: #CC0000;
}
.box_gray {
  font-family: Arial;
  font-size: 11px;
  background-color: #CCCCCC;
  border: thin solid #333333;
  padding: 1px;
  margin: 1px;
}
.title_white {
  font-family: Arial;
  font-size: 10px;
  background-color: #FFFFFF;
  border: thin dashed #666666;
  vertical-align: middle;
}
.title_report_white {
  font-family: Arial;
  font-size: 15px;
  background-color: #FFFFFF;
  border: thin solid #333333;
  padding: 1px;
  margin: 1px;
}
</style>
</head>



<body>


<script type="text/javascript">
var stopv=0;
var reLoadtimer=setInterval("stopsend();", 5000 );
function stopsend()
{
stopv=1;
clearInterval(reLoadtimer);
}
function movef0()
{
if(stopv==1)
{
location.href='/R3EMSAPP_EDM.edm?mode=monitor&submode=ems&refresh=0';
}
else
{
alert('wait some sec');
}
}
</script>


<hr>(2025-9-21, 12:49:08) --- EMS Monitoring EMS-data
.... <input type=button value="Refresh"  onClick="movef0()" class=styellow style="width:120px"> ....
[ <a href="/R3EMSAPP_EDM.edm?mode=monitor&submode=ems&refresh=1"> Auto View </a> ]     

</center><hr>

<table style="width:700px; margin:1px; border-spacing:1px; background-color:#FFFFFF; border-collapse:collapse; border: 1px solid #666666;">

<tr><td style="background-color:#DDFFFF;vertical-align:top;">

<table style="width:450px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=5 style="background-color:#444444;color:white;"> EMS Information </td></tr>

<tr><td width=90 align=center rowspan=2 style="background-color:#CCCCFF;"> EMS </td><td width=90 align=center style="background-color:#CCCCFF;"> Mode </td><td width=90 align=center style="background-color:#CCCCFF;"> SOM </td><td width=90 align=center style="background-color:#CCCCFF;"> PCM </td><td width=90 align=center style="background-color:#CCCCFF;"> Target Power </td></tr>
<tr><td width=90 align=center style="background-color:#CCCCFF;"> ELA </td><td width=90 align=center style="background-color:#CCCCFF;"> SEA </td><td width=90 align=center style="background-color:#CCCCFF;"> Auto-Strong </td><td width=90 align=center style="background-color:#CCCCFF;"> 4503 </td></tr>
<tr><td width=90 align=center style="background-color:#CCFFCC;"> ELA </td><td width=90 align=center style="background-color:#CCFFCC;"> - </td><td width=90 align=center style="background-color:#CCFFCC;"> - </td><td width=90 align=center style="background-color:#CCFFCC;"> Auto-Strong </td><td width=90 align=center style="background-color:#CCFFCC;"> 0 </td></tr>
<tr><td width=90 align=center> ETS </td><td width=90 align=center> - </td><td width=90 align=center> - </td><td width=90 align=center> Unknown </td><td width=90 align=center> 0 </td></tr>
<tr><td width=90 align=center> ERM </td><td width=90 align=center> - </td><td width=90 align=center> - </td><td width=90 align=center> NOP </td><td width=90 align=center> 0 </td></tr>
<tr><td width=90 align=center> ELM </td><td width=90 align=center> - </td><td width=90 align=center> - </td><td width=90 align=center> NOP </td><td width=90 align=center> 0 </td></tr>
<tr><td width=90 align=center> PEM </td><td width=90 align=center> - </td><td width=90 align=center> - </td><td width=90 align=center> Unknown </td><td width=90 align=center> 0 </td></tr>
<tr><td width=90 align=center style="background-color:#FFCCCC;"> PCS </td><td width=90 align=center style="background-color:#FFCCCC;"> - </td><td width=90 align=center style="background-color:#FFCCCC;"> SEA </td><td width=90 align=center style="background-color:#FFCCCC;"> Auto-Strong </td><td width=90 align=center style="background-color:#FFCCCC;"> 5325 </td></tr></table>

<table style="width:450px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=5 style="background-color:#444444;color:white;"> EMS Flags </td></tr>

<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=2> System </td><td width=90 align=center style="background-color:#CDC9C9;"> Ready </td><td width=90 align=center style="background-color:#CDC9C9;"> Fault </td><td width=90 align=center style="background-color:#CDC9C9;">  </td><td width=90 align=center style="background-color:#CDC9C9;">  </td></tr>
<tr><td width=90 align=center> 1 </td><td width=90 align=center> 0 </td><td width=90 align=center> </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=4> Status </td><td width=90 align=center style="background-color:#CDC9C9;"> PV-Output </td><td width=90 align=center style="background-color:#CDC9C9;"> Grid-Chrg </td><td width=90 align=center style="background-color:#CDC9C9;"> Batt-Dischrg </td><td width=90 align=center style="background-color:#CDC9C9;"> Auto-OW </td></tr>
<tr><td width=90 align=center> 1 </td><td width=90 align=center> 1 </td><td width=90 align=center> 1 </td><td width=90 align=center> 1 </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;"> Auto-OS </td><td width=90 align=center style="background-color:#CDC9C9;"> Auto-WS </td><td width=90 align=center style="background-color:#CDC9C9;"> </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 1 </td><td width=90 align=center> 1 </td><td width=90 align=center> </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=2> Communication </td><td width=90 align=center style="background-color:#CDC9C9;"> PCS (CAN) </td><td width=90 align=center style="background-color:#CDC9C9;"> SM (RS485) </td><td width=90 align=center style="background-color:#CDC9C9;"> Remote (LAN) </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 1 </td><td width=90 align=center> 1 </td><td width=90 align=center> 1 </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=2> Jumper </td><td width=90 align=center style="background-color:#CDC9C9;"> IP </td><td width=90 align=center style="background-color:#CDC9C9;"> PBA </td><td width=90 align=center style="background-color:#CDC9C9;"> TS </td><td width=90 align=center style="background-color:#CDC9C9;"> SIM </td></tr>
<tr><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=4> Remote </td><td width=90 align=center style="background-color:#CDC9C9;"> Download </td><td width=90 align=center style="background-color:#CDC9C9;"> Manual </td><td width=90 align=center style="background-color:#CDC9C9;"> Auto </td><td width=90 align=center style="background-color:#CDC9C9;"> Weather </td></tr>
<tr><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> 1 </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;"> Price </td><td width=90 align=center style="background-color:#CDC9C9;"> </td><td width=90 align=center style="background-color:#CDC9C9;"> </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 1 </td><td width=90 align=center> </td><td width=90 align=center> </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=2> EDM </td><td width=90 align=center style="background-color:#CDC9C9;"> Manual </td><td width=90 align=center style="background-color:#CDC9C9;"> Local Auto </td><td width=90 align=center style="background-color:#CDC9C9;"> </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=6> PEM </td><td width=90 align=center style="background-color:#CDC9C9;"> Enable </td><td width=90 align=center style="background-color:#CDC9C9;"> Control Enable </td><td width=90 align=center style="background-color:#CDC9C9;"> Control Mode</td><td width=90 align=center style="background-color:#CDC9C9;"> Mode(ENG)</td></tr>
<tr><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> unknown </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;"> CN Status </td><td width=90 align=center style="background-color:#CDC9C9;"> G_Set_Point</td><td width=90 align=center style="background-color:#CDC9C9;"> Feed-in_limit</td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> 60 </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;"> T_MIN_SOC </td><td width=90 align=center style="background-color:#CDC9C9;"> T_MIN_Ariv</td><td width=90 align=center style="background-color:#CDC9C9;"> T_MAX_SOC</td><td width=90 align=center style="background-color:#CDC9C9;"> T_MAX_Ariv</td></tr>
<tr><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td></tr></table>

<table style="width:450px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=5 style="background-color:#444444;color:white;"> EMS Values </td></tr>

<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=4> Power </td><td width=90 align=center style="background-color:#CDC9C9;"> PV (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> Inverter (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> Load (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> Grid (W) </td></tr>
<tr><td width=90 align=center> 1005.0 </td><td width=90 align=center> 800.0 </td><td width=90 align=center> 760.6 </td><td width=90 align=center> -39.4 </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;"> PV(User) (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> BDC (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> Load-10s (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 1005.0 </td><td width=90 align=center> 356.0 </td><td width=90 align=center> 822.8 </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=2> Temperature </td><td width=90 align=center style="background-color:#CDC9C9;"> System (C) </td><td width=90 align=center style="background-color:#CDC9C9;"> </td><td width=90 align=center style="background-color:#CDC9C9;"> </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 34.0 </td><td width=90 align=center> </td><td width=90 align=center> </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=4> Install Options </td><td width=90 align=center style="background-color:#CDC9C9;"> PV1 Pwr (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> PV2 Pwr (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> Inv Pwr (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> Grid Freq (Hz) </td></tr>
<tr><td width=90 align=center> 3960 </td><td width=90 align=center> 3960 </td><td width=90 align=center> 8000 </td><td width=90 align=center> 50 </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;"> FeedIn Limit (%) </td><td width=90 align=center style="background-color:#CDC9C9;"> ELA Simple Type (W) </td><td width=90 align=center style="background-color:#CDC9C9;"> Sleep Mode </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 60 </td><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> </td></tr>
</table>

<table style="width:450px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=5 style="background-color:#444444;color:white;"> PCS Flags </td></tr>

<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=2> System </td><td width=90 align=center style="background-color:#CDC9C9;"> Ready </td><td width=90 align=center style="background-color:#CDC9C9;"> Warning </td><td width=90 align=center style="background-color:#CDC9C9;"> Fault </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 1 </td><td width=90 align=center> 0 </td><td width=90 align=center> 0 </td><td width=90 align=center> </td></tr>
</table>

<table style="width:450px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=5 style="background-color:#444444;color:white;"> BMS Information </td></tr>

<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=2> Flags </td><td width=90 align=center style="background-color:#CDC9C9;"> Batt-Chrg </td><td width=90 align=center style="background-color:#CDC9C9;"> Batt-Dischrg </td><td width=90 align=center style="background-color:#CDC9C9;"> </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 1 </td><td width=90 align=center> 0 </td><td width=90 align=center> </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=2> Values </td><td width=90 align=center style="background-color:#CDC9C9;"> SOC (%) </td><td width=90 align=center style="background-color:#CDC9C9;"> SOH (%) </td><td width=90 align=center style="background-color:#CDC9C9;"> Module Qty. </td><td width=90 align=center style="background-color:#CDC9C9;"> Cell Qty. </td></tr>
<tr><td width=90 align=center> 14.0 </td><td width=90 align=center> 95.0 </td><td width=90 align=center> 4 </td><td width=90 align=center> 32 </td></tr>
</table>

<table style="width:450px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=5 style="background-color:#444444;color:white;"> SM(Smart Meter) Information </td></tr>

<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=2> Flags </td><td width=90 align=center style="background-color:#CDC9C9;"> Connection </td><td width=90 align=center style="background-color:#CDC9C9;"> </td><td width=90 align=center style="background-color:#CDC9C9;"> </td><td width=90 align=center style="background-color:#CDC9C9;"> </td></tr>
<tr><td width=90 align=center> 1 </td><td width=90 align=center> </td><td width=90 align=center> </td><td width=90 align=center> </td></tr>
<tr><td width=90 align=center style="background-color:#CDC9C9;" rowspan=4> Values </td><td width=180 align=center style="background-color:#CDC9C9;" colspan=2> Feed-In Total-Wh (Wh) </td><td width=180 align=center style="background-color:#CDC9C9;" colspan=2> Purchased Total-Wh (Wh) </td></tr>
<tr><td width=180 align=center colspan=2> 19547292.826 </td><td width=180 align=center colspan=2> 12831415.632 </td></tr>
<tr><td width=180 align=center style="background-color:#CDC9C9;" colspan=2> Total-W (W) </td><td width=180 align=center style="background-color:#CDC9C9;" colspan=2> Total-Wh (Wh) </td></tr>
<tr><td width=180 align=center colspan=2> 15.4 </td><td width=180 align=center colspan=2> -6715877.2 </td></tr>
</table>

</td><td style="background-color:#FFDDFF; vertical-align:top;">

<table style="width:350px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td width=200 style="background-color:#000077; color:#FFFFFF;">HW Version</td>     

<td width=150>0</td></tr></table>
<table style="width:350px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=4 style="background-color:#444444;color:white;"> HW Jumper (now writing = 0)</td></tr>
<td width=120>Static IP</td><td width=55>0</td> <td width=120>PBA Inspection</td><td width=55>0</td></tr>
<tr><td>Time Schedule</td><td>0</td> <td>Manual Control</td><td>0</td></tr>
</table>

<table style="width:350px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=4 style="background-color:#444444;color:white;"> HW ADC (now writing = 0)</td></tr>
<td width=120>Bd Temperature</td><td width=55>34.0</td> <td width=120>&nbsp;</td><td width=55>&nbsp;</td></tr>
<tr><td>D-12V</td><td>0.0</td> <td>D-5V</td><td>0.0</td></tr>
<tr><td>D-3.3V</td><td>0.0</td> <td>D-1.8V</td><td>0.0</td></tr>
<tr><td>D-1.2V</td><td>0.0</td> <td>D-BAT</td><td>0.0</td></tr>
<tr><td>D-Coin Cell</td><td>0.0</td> <td>&nbsp;</td><td>&nbsp;</td></tr>
</table>

<table style="width:350px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td width=200 rowspan=5 style="background-color:#000077; color:#FFFFFF;">inner IP Address(1)</td>
<td width=150>192.168.178.36</td></tr></table>
<table style="width:350px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=5 style="background-color:#444444;color:white;"> 10sec avg. Value </td></tr>

<tr><td width=70 rowspan=5 style="background-color:#000077; color:#FFFFFF;">Power [W]</td>

<td width=80>Grid</td><td width=60 align=center>-9.0</td> <td width=80>Load</td><td width=60 align=center>822.8</td></tr>
<tr><td>Load:PCS</td><td align=center>0.0</td> <td>EV:PCS</td><td align=center>0.0</td></tr>
<tr><td>PV</td><td align=center>977.0</td> <td>PV:User</td><td align=center>977.0</td></tr>
<tr><td>INV:PCS</td><td align=center>831.8</td> <td> &nbsp; </td><td align=center> &nbsp; </td></tr>
<tr><td>Battery</td><td align=center>275.1</td> <td> &nbsp; </td><td align=center> &nbsp; </td></tr>
</table>

<table style="width:350px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=5 style="background-color:#444444;color:white;"> Today Wh Value </td></tr>

<tr><td width=70 rowspan=6 style="background-color:#000077; color:#FFFFFF;">[Wh]</td>  

<td width=80>Grid-Pur</td><td width=60 align=center>1704</td> <td width=80>Grid-Feed</td><td width=60 align=center>35</td></tr>
<tr><td>Load</td><td align=center>6260</td> <td>&nbsp;</td><td align=center>&nbsp;</td></tr>
<tr><td>Load:PCS</td><td align=center>0</td> <td>EV:PCS</td><td align=center>0</td></tr>
<tr><td>PV</td><td align=center>1715</td> <td>PV:User</td><td align=center>1703</td></tr>
<tr><td>INV-Pur</td><td align=center>0</td> <td>INV-Feed</td><td align=center>4460</td></tr>
<tr><td>Bat-Ch</td><td align=center>640</td> <td>Bat-Dis</td><td align=center>3371</td></tr>
</table>

<table style="width:350px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=5 style="background-color:#444444;color:white;"> TOTAL kWh Value </td></tr>

<tr><td width=70 rowspan=6 style="background-color:#000077; color:#FFFFFF;">[kWh]</td> 

<td width=80>Grid-Pur</td><td width=60 align=center>130</td> <td width=80>Grid-Feed</td><td width=60 align=center>409</td></tr>
<tr><td>Load</td><td align=center>752</td> <td>&nbsp;</td><td align=center>&nbsp;</td></tr>
<tr><td>Load:PCS</td><td align=center>0</td> <td>EV:PCS</td><td align=center>0</td></tr>
<tr><td>PV</td><td align=center>1051</td> <td>PV:User</td><td align=center>1046</td></tr>
<tr><td>INV-Pur</td><td align=center>0</td> <td>INV-Feed</td><td align=center>1033</td></tr>
<tr><td>Bat-Ch</td><td align=center>303</td> <td>Bat-Dis</td><td align=center>269</td></tr>
</table>

</td><td style="background-color:#FFDDFF; vertical-align:top;">

<table style="width:350px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=4 style="background-color:#444444;color:white;"> ELA PV-Forecast Hour </td></tr>

<td width=55 align=center>Hour</td><td width=120>Wh</td> <td width=55 align=center>Hour</td><td width=120>Wh</td></tr>

<td align=center>0</td><td>0</td> <td align=center>12</td><td>2467</td></tr>
<td align=center>1</td><td>0</td> <td align=center>13</td><td>2682</td></tr>
<td align=center>2</td><td>0</td> <td align=center>14</td><td>2419</td></tr>
<td align=center>3</td><td>0</td> <td align=center>15</td><td>2249</td></tr>
<td align=center>4</td><td>0</td> <td align=center>16</td><td>1949</td></tr>
<td align=center>5</td><td>0</td> <td align=center>17</td><td>1865</td></tr>
<td align=center>6</td><td>0</td> <td align=center>18</td><td>1473</td></tr>
<td align=center>7</td><td>832</td> <td align=center>19</td><td>277</td></tr>
<td align=center>8</td><td>498</td> <td align=center>20</td><td>0</td></tr>
<td align=center>9</td><td>941</td> <td align=center>21</td><td>0</td></tr>
<td align=center>10</td><td>1175</td> <td align=center>22</td><td>0</td></tr>
<td align=center>11</td><td>1555</td> <td align=center>23</td><td>0</td></tr>
</table>

</td></tr><tr><td colspan=2 style="background-color:#FFFFFF; vertical-align:top;">     

<table style="width:700px; margin:2px; border-spacing:1px; background-color:#0000FF; border-collapse:collapse; border: 1px solid #666666; padding:2px;">

<tr><td align=center colspan=8 style="background-color:#444444;color:white;"> EMS S/W Status </td></tr>

<tr><td align=center style="background-color:#CCCCCC;" rowspan=2> S/W name </td>       

    <td align=center style="background-color:#CCCCCC;" colspan=5> status </td>

    <td align=center style="background-color:#CCCCCC;" colspan=2> run-time </td></tr>  

<tr><td align=center style="background-color:#CCCCCC;"> Ver </td>

    <td align=center style="background-color:#CCCCCC;"> Init </td>

    <td align=center style="background-color:#CCCCCC;"> Pause </td>

    <td align=center style="background-color:#CCCCCC;"> Exit </td>

    <td align=center style="background-color:#CCCCCC;"> nice </td>

    <td align=center style="background-color:#CCCCCC;"> Secs </td>

    <td align=center style="background-color:#CCCCCC;"> Start </td></tr>

<tr><td> EMS-Main </td>

<td>V.010006</td><td>1</td><td>0</td><td>0</td><td>0</td> <td>4166043</td><td>2025-08-04,07:31:03</td></tr>
<tr><td> EMS-BMS </td>

<td>V.010000</td><td>1</td><td>0</td><td>0</td><td>0</td> <td>4157782</td><td>2025-08-04,07:31:09</td></tr>
<tr><td> EMS-EDM </td>

<td>V.010002</td><td>1</td><td>0</td><td>0</td><td>0</td> <td>0</td><td>2025-09-21,12:49:08</td></tr>
<tr><td> EMS-ELA </td>

<td>V.040001</td><td>1</td><td>0</td><td>0</td><td>0</td> <td>4163088</td><td>2025-08-04,07:31:10</td></tr>
<tr><td> EMS-HW Infor.</td>

<td>V.010001</td><td>1</td><td>0</td><td>0</td><td>0</td> <td>4034525</td><td>2025-08-04,07:31:05</td></tr>
<tr><td> EMS-LOG </td>

<td>V.010003</td><td>1</td><td>0</td><td>0</td><td>0</td> <td>4162535</td><td>2025-08-04,07:31:04</td></tr>
<tr><td> EMS-Meter </td>

<td>V.010000</td><td>1</td><td>0</td><td>0</td><td>0</td> <td>4166037</td><td>2025-08-04,07:31:07</td></tr>
<tr><td> EMS-M2M </td>

<td>V.010003</td><td>1</td><td>0</td><td>0</td><td>0</td> <td>4166037</td><td>2025-08-04,07:31:11</td></tr>
</table>

</td><td>

</td></tr></table>

</body>
</html>
"""

def test(teststr):
    meter_data = extract_today_wh_values(teststr)
    print(f"meter_data: {meter_data}")

if __name__ == '__main__':
    test(TEST_STR)