var div = document.createElement('div');
div.innerHTML = `<div class="alert alert-warning alert-dismissible fade show" role="alert">
    < strong > The student of name is { { toast } }, has been deleted of roll no { { toast1 } }</strong > You should check in on some of those fields below.
 < button type = "button" class="btn-close" data - bs - dismiss="alert" aria - label="Close" ></button >
</div > `;

document.body.insertBefore(div,document.getElementsByTagName('deleteStudent '))