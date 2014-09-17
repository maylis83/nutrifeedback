$(document).ready(function(){
  function populate_calendar_selects(dateText, inst, month_id, day_id, year_id) {
     console.log("populate");
     date = dateText.match(/^(\d{2})\s(\d{2})\s(\d{4})/);
     console.log(date);
     $('#' + month_id).val(parseInt(date[1]));
     $('#' + day_id).val(parseInt(date[2]));
     $('#' + year_id).val(parseInt(date[3]));
  }

  function set_month_length(month_id, day_id, year_id) {
      var month = $("#" + month_id + " :selected").text();

      // baseline is 31 days
      if ($("#" + day_id + " option[value='29']").length == 0) {
         $("#" + day_id).append('<option value="29">29</option>')
      }

      if ($("#" + day_id + " option[value='30']").length == 0) {
         $("#" + day_id).append('<option value="30">30</option>')
      }

      if ($("#" + day_id + " option[value='31']").length == 0) {
         $("#" + day_id).append('<option value="31">31</option>')
      }

      switch(month) {
         case 'February':
            $("#" + day_id + " option[value='31']").remove();
            $("#" + day_id + " option[value='30']").remove();

            var year = parseInt($("#" + year_id + " :selected").text());

            // if not leap year, remove 29
            if (!(((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0))) {
              $("#" + day_id + " option[value='29']").remove();
            }
            break;
         case 'April':
         case 'June':
         case 'September':
         case 'November':
            $("#" + day_id + " option[value='31']").remove();
            break;
      }
    }
}
