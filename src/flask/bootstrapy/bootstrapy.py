def build_2x2_grid(c1, c2, c3, c4):
    return build_container (build_row (build_col_md(c1, 6, 100) + build_col_md(c2, 6, 100), 50) + build_row (build_col_md(c3, 6, 100) + build_col_md(c4, 6, 100), 50))

def build_container(content):
    return '<div class="container-fluid">' + content + '</div>'

def build_col_md(content, nb, height):
    return '<div class="col-md-' + str(nb) + '" style="height: ' + str(height) + '%">'+ content + '</div>'

def build_row(content, height):
    return '<div class="row" style="height: ' + str(height) + '%">'+ content + '</div>'

def build_well(content):
    return '<div class="well" style="height: 90%">' + content + '</div>'
