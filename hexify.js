function ConvertStringToHex(str) {
    var arr = [];
        for (var i = 0; i < str.length; i++) {
            arr[i] = ("00" + str.charCodeAt(i).toString(16)).slice(-4);
        }
    return "\\u" + arr.join("\\u");
}

function ConvertHexToString(Hex) {
    var hex = Hex.toString();
    var str = '';
    for (var i = 0; i < hex.length; i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

var str = "This is a sample string to be secured";

var str_to_hex = ConvertStringToHex(str)
console.log(str_to_hex);

var hex_to_str = ConvertHexToString(str_to_hex)
console.log(hex_to_str);
