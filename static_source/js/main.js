function populate_calendar_selects(dateText, inst, month_id, day_id, year_id) {
   console.log("populate");
   date = dateText.match(/^(\d{2})\s(\d{2})\s(\d{4})/);
   console.log(date);
   $('#' + month_id).val(parseInt(date[1]));
   $('#' + day_id).val(parseInt(date[2]));
   $('#' + year_id).val(parseInt(date[3]));
}
