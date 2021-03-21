var = "dfdf"

# 1
var = var.lower()

# 2
for i in range(33, 44):
    var = var.replace(chr(i), "")
var = var.replace(chr(47), "")
for i in range(91, 94):
    var = var.replace(chr(i), "")
var = var.replace(chr(96), "")
for i in range(123, 126):
    var = var.replace(chr(i), "")

# 3
i = 0
while i >= len(var) - 1:
    if (var[i] == var[i + 1]):
        var = var.pop(i)
        i = i + 1
    i = i - 1
answer = var