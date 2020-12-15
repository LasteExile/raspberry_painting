var penColor = "255, 255, 255"
console.log(active_page)
renderField()
var amount_of_pages = field['length']
console.log(field)
for (i = 1; i < amount_of_pages; i++) {
    page_num = i + 1
    $('.page.add').before('<div class="page ' + page_num + '" onclick="moveToPage(' + page_num + ')">' + page_num + '</div>')
}
$(".active").css("color", "rgb(0, 0, 0)").css("background-color", "rgb(255, 255, 255)").removeClass("active")
$("." + (active_page + 1)).addClass("active")
$(".active").css("color", "rgb(255, 255, 255)").css("background-color", "rgb(0, 0 , 0)")


function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

function runAnimation() {
    reapets = $("#reapets").val()
    delay = $("#delay").val()
    $.ajax({
        type: 'GET',
        async: true,
        url: '/update_pixels',
        data: "timeout=" + delay + "&reapets=" + reapets,
        success: function(data) {
        },
        dataType: 'json',
        });
}

function RenderAnimation() {

}

function renderField() {
  for (var i = 0; i < 16; i++) {
    for (var j = 0; j < 16; j++) {
      color = field[active_page][i][j][2]
      $('.y'+ i + 'x' + j).css('background-color', `rgb(${color})`)
    }
  }
}

function clearSession() {
  $.ajax({
    type: 'GET',
    async: true,
    url: '/update_pixels',
    data: "clear_session=1",
    success: function(data) {
    },
    dataType: 'json',
  });
  alert("Reload page")
  //document.location.reload()
}


function moveToPage(page) {
  active_page = page - 1
  renderField()
  $(".active").css("color", "rgb(0, 0, 0)").css("background-color", "rgb(255, 255, 255)").removeClass("active")
  $("." + page).addClass("active")
  $(".active").css("color", "rgb(255, 255, 255)").css("background-color", "rgb(0, 0 , 0)")
  $.ajax({
    type: 'GET',
    async: true,
    url: '/update_pixels',
    data: "active_page=" + (active_page),
    success: function(data) {
    },
    dataType: 'json',
  });
  console.log(page)
}


function addPage() {
  page_num = $('.page');
  last_element_index = page_num['length'] - 2;
  page_num = parseInt(page_num[last_element_index].className.split(' ')[1]) + 1;
  $('.page.add').before('<div class="page ' + page_num + '" onclick="moveToPage(' + page_num + ')">' + page_num + '</div>')
  page_num--
  active_page = page_num
  $.ajax({
    type: 'GET',
    async: true,
    url: '/add_page',
    success: function(data) {
      field.push(data['field'])
   //   console.log(field)
    },
    dataType: 'json',
  });
}


function setPixelColor(pixel, id) {
  coords = id.split(' ')
  field[active_page][coords[0]][coords[1]][2] = penColor
  pixel.style.backgroundColor = "rgb(" +  penColor + ")"
  $.ajax({
    type: 'GET',
    async: true,
    url: '/update_pixels',
    data: "page=" + active_page +"&pixel_id="+id + "&color=" + penColor,
    success: function(data) {
      //console.log(data)
    },
    dataType: 'json',
  });
}


function clearAll() {
  $.ajax({
    type: 'GET',
    async: true,
    url: '/update_pixels',
    data: "page=" + active_page + "&clear=1",
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
