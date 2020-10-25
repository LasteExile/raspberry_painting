var penColor = "255, 255, 255"

function setPixelColor(pixel, id) {
  pixel.style.backgroundColor = "rgb(" +  penColor + ")"
  $.ajax({
    type: 'GET',
    async: true,
    url: '/update_pixels',
    data: "pixel_id="+id + "&color=" + penColor,
    success: function(data) {
      console.log(id)
    },
    dataType: 'json',
  });
}


function clearAll() {
  $.ajax({
    type: 'GET',
    async: true,
    url: '/update_pixels',
    data: "clear=1",
    success: function(data) {
      console.log("Done")
    },
    dataType: 'json',
  });
  $(".pixel").css("background-color", "rgb(255, 255, 255)")
}

function setColor(color) {
  choosenPen = document.getElementsByClassName("choosenPen")[0]
  penColor = color
  choosenPen.style.backgroundColor = "rgb(" +  penColor + ")"
}
