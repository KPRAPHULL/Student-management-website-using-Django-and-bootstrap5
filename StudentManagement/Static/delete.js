
var div =`<div class="alert alert-warning alert-dismissible fade show" role="alert">
<strong>Can't update,no student record found </strong> Please add new Record
<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>`

document.body.insertBefore(div,document.getElementById('delStudent'));
// document.body.innerHTML=div;
// document.body.appendChild(div) 