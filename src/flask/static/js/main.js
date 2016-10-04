var list_id = new Array();
var list_interval = new Array();
var c = "";
var json = "";

function change_background(element, color) {
  element.style.backgroundColor = color;
}

function build_well(content, id) {
  if (id === "")
  return '<div class="well" style="height: 100%; width: 100%;">' + content + '</div>';
  else
  return '<div id="' + id + '_grid" class="well" style="height: 100%; width: 100%;">' + content + '</div>';
}

function build_container(content) {
  return '<div class="container-fluid">' + content + '</div>';
}

function build_col_md(content, nb, height) {
  return '<div class="col-md-' + nb + '" style="height: ' + height + '%; padding: 0 !important;margin: 0 !important;">' + content + '</div>';
}

function build_row(content) {
  return '<div class="row">'+ content + '</div>';
}

function build_2x1_grid(c1, c2) {
  return build_container (build_row (build_col_md(c1, 6, 100) + build_col_md(c2, 6, 100), 100));
}

function build_2x2_grid(c1, c2, c3, c4) {
  return build_container (build_row (build_col_md(c1, 6, 100) + build_col_md(c2, 6, 100), 50) + build_row (build_col_md(c3, 6, 100) + build_col_md(c4, 6, 100), 50))
}

function build_grid(list_modules, count) {
  if (count === 0) {
    return "No modules";
  }
  if (count === 1) {
    var m = list_modules.pop();
    return build_well(m[0], m[1]);
  }
  if (count === 2) {
    var m1 = list_modules.pop();
    var m2 = list_modules.pop();
    return build_2x1_grid(build_well(m1[0], m1[1]), build_well(m2[0], m2[1]));
  }
  var l1 = [[], [], [], []];
  var i = 0;
  while (list_modules.length > 0) {
    l1[i % 4] = l1[i % 4] + [list_modules.pop()];
    i = i + 1;
  }

  return build_2x2_grid(build_grid(l1[0]), build_grid(l1[1]), build_grid(l1[2]),build_grid(l1[3]));
}

function remove_module(e) {
  remove(list_id, e);
  clearInterval(list_interval[e]);
  if ($("#" + e + "_grid").get(0) != undefined)
    $("#" + e + "_grid").get(0).outerHTML = "";
}

function remove(arr, item) {
  for(var i = arr.length; i--;) {
    if(arr[i] === item) {
        arr.splice(i, 1);
    }
  }
}

function update_module(e) {
  $.ajax({
    async: false,
    type: 'GET',
    url: $SCRIPT_ROOT + "/get_from_module/" + e,
    success: function(content_module){
      $("#" + e + "_grid").html('<div class="thumbnail">'+ content_module + '</div>');
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      remove_module(e);
    }
  });
}

setInterval(update_panel, 10000);
function update_panel() {
  $.ajax({
    url: $SCRIPT_ROOT + "/module/list",
    type: 'GET',
    success: function(data){
      json = JSON.parse(data);
      $("#panel").empty();

      for(var elt in json) {
        $("#panel").html($("#panel").html() + '<button id="' + elt + '_button" type="button" class="btn btn-primary" style="width:100%">' + json[elt] + '</button>');
      }

      $("#panel").html(build_well($("#panel").html()));

      for (var elt in json) {
        (function(elt, json) {
          $("#" + elt + "_button").click(function() {
            $("#" + elt + "_grid").fadeToggle();
          });
        })(elt, json)
      }

      update_content();
    },
    error: function(data) {
      for (var i in list_id)
        clearInterval(list_interval[i]);
      list_id = new Array();
      $("#panel").html(build_well(""));
      $("#content").html(build_container(build_row("")));
    }
  });
}

function update_content() {
  c = "";
  var count = 0;
  for(var elt in json) {
    (function(e, j) {
      if (!list_id.includes(e)) {
        count += 1;
        list_id.push(e);
        list_interval[e] = setInterval(update_module.bind("", e), 10000);

        c += '<div id="' + e + '_grid" class="col-md-6" style="padding: 0 !important;margin: 0 !important; width: 50%;"><div class="thumbnail">Loading...</div></div>';
        if (count % 2 === 0)
          c += '<div class="clearfix visible-md-block"></div>';
      }
      else {
        count += 1;
        if ($("#" + e + "_grid").get(0) != undefined)
          c += $("#" + e + "_grid").get(0).outerHTML;
        if (count % 2 === 0)
          c += '<div class="clearfix visible-md-block"></div>';
      }
    })(elt, json)
  }

  for (var l in list_id) {
    if (!(l in json)) {
      remove_module(l);
    }
  }

  $("#content").html(build_container(build_row(c)));

  for(var elt in json) {
    update_module(elt);
  }
}

$("#content").html(build_container(build_row("")));
update_panel();
