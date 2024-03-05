function getJson() {
    try {
        return JSON.parse($('#json-input').val());
    } catch (ex) {
        alert('Wrong JSON Format: ' + ex);
    }
}

var editor = new JsonEditor('#json-display', getJson());
$('#translate').on('click', function () {
    editor.load(getJson());
});