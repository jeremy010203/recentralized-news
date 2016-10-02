def build_2x2_grid(c1, c2, c3, c4):
    return build_container (build_row (build_col_md(c1, 6, 100) + build_col_md(c2, 6, 100), 50) + build_row (build_col_md(c3, 6, 100) + build_col_md(c4, 6, 100), 50))

def build_2x1_grid(c1, c2):
    return build_container (build_row (build_col_md(c1, 6, 100) + build_col_md(c2, 6, 100), 100))

def build_container(content):
    return '<div class="container-fluid">' + content + '</div>'

def build_col_md(content, nb, height):
    return '<div class="col-md-' + str(nb) + '" style="height: ' + str(height) + '%; padding: 0 !important;margin: 0 !important;">'+ content + '</div>'

def build_row(content, height):
    return '<div class="row" style="height: ' + str(height) + '%">'+ content + '</div>'

def build_border(content):
    return '<div style="height: 100%; width: 100%; border: 1px solid black;">' + content + '</div>'

def build_well(content):
    return '<div class="well" style="height: 100%; width: 100%;">' + content + '</div>'

def build_side_panel(left, right):
    return build_row(build_col_md(left, 2, 100) + build_col_md(right, 10, 100), 100)

def build_grid(list_modules):
    if (len(list_modules) == 0):
        return ""
    if (len(list_modules) == 1):
        return list_modules.pop()
    if (len(list_modules) == 2):
        return build_2x1_grid(list_modules.pop(), list_modules.pop())
    l1 = [[], [], [], []]
    i = 0
    while (len(list_modules) > 0):
        l1[i % 4] = l1[i % 4] + [list_modules.pop()]
        i = i + 1
    return build_2x2_grid(build_grid(l1[0]), build_grid(l1[1]), build_grid(l1[2]),build_grid(l1[3]))
