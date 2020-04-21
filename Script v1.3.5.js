function sendEmail(e) {
  var values = e.values;
  Logger.log(values);
  var ss = SpreadsheetApp.getActive();
  var sheet = ss.getSheetByName("Risposte del modulo 1");
  var headers = sheet.getRange(1,1,1,sheet.getLastColumn()).getValues();
  var htmlBody = "<table border='1'>";
  for (var i=0; i < values.length; i++) {
      var label = headers[0][i];
      var data = values[i];    
      Logger.log(label + ": " + data);
      htmlBody += "<tr><td>" + label + ": </td><td><b>" + data.toString().replace(/(\r\n|\n|\r)/gm, "<br>") + "</b></tr>";
  }
  htmlBody += "</table>";
  Logger.log(htmlBody);
  var name = values[3];
  var SendTo = "rondinix@gmail.com";
  var Subject = "Nuovo ordine da " + name;
  if (htmlBody) {
      GmailApp.sendEmail(
        SendTo,
        Subject,
      '',{
      from : 'rondinix@gmail.com',
      replyto: 'rondinix@gmail.com',
      htmlBody: htmlBody,
      });
      
    }
  Logger.log('Email sent: '+Subject);

  var ssdest = SpreadsheetApp.openById("1DVwIfpyzXj-ov00Qlv_IBOmAgCs70WMeHsm10azVMXY");
  var sheetdest = ssdest.getSheetByName("MASTER");
  var lastRow = sheetdest.getLastRow();
  for (var i=0; i < values.length; i++) {
    sheetdest.getRange(lastRow+1, i+1).setValue(values[i]);
    sheetdest.getRange(lastRow+1, 28).setValue(lastRow);
  }
  
  var fogli = ["ORT", "PES", "MAC", "PAN", "TAG", "SUR", "FRG", "PRF", "DET", "DSP", "MON", "NFD", "FAR", "LAC"]
  for (var i=0; i < fogli.length; i++) {
    sheetdest = ssdest.getSheetByName(fogli[i]);
    sheetdest.getRange(lastRow+1, 1).setValue(values[3]);
    sheetdest.getRange(lastRow+1, 2).setValue(values[5]);
    sheetdest.getRange(lastRow+1, 3).setValue(values[0]);
    sheetdest.getRange(lastRow+1, 4).setValue(values[8+i]);
    sheetdest.getRange(lastRow+1, 5).setValue(lastRow);
  }

}