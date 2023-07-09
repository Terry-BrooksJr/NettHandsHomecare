// SECTION - Profile Editabiity Toggle

const editProfileButton = document.getElementById("edit-button")
const cancelChangesButton = document.getElementById("reset-id-cancel")
const saveChangeButton = document.getElementById("submit-id-save")

function makeProfileEditable() {
  const editableFields = document.querySelectorAll('.editable')
  editableFields.forEach((field) => {
    field.removeAttribute('readonly')
  })
  saveChangeButton.removeAttribute('hidden')
  cancelChangesButton.removeAttribute('hidden')
  editProfileButton.hidden = true
}

function cancelPendingEdits() {
  window.location.reload();
}

function makeProfileUnEditable() {
  const editableFields = document.querySelectorAll('.editable')
  console.log('Called')
  editableFields.forEach((field) => {
    console.log(field)
    field.disabled = true
    console.log(`${field} is disabled`)
  })
  cancelChangesButton.hidden = true
  saveChangeButton.hidden = true
}
cancelChangesButton.addEventListener('click', cancelPendingEdits)
editProfileButton.addEventListener('click', makeProfileEditable)
window.addEventListener('load', makeProfileUnEditable)

// !SECTION

// SECTIION - Client Submission Filtering & Pagination
const $submissions = document.querySelectorAll(".client-submission")
const $page = $('.page');
const $pagination = $('.pagination');
const $paginationList = $('.pagination');
const $submissionSearch = $('.search-field');
const itemTotal = 10;

console.log($submissionSearch)
// hide all
function hideAll() {
  
  $submissions.forEach((field) => {
    field.hidden = true
  })
}


// display first 10
function displayRange(a, b) {
  hideAll();
  // display 0 - 1 students
  $submissions.slice(a, b).fadeIn();
}

displayRange(0, itemTotal);

// create pagination links
let pagination = '';
for (var i = 0; i <= $submissions.length / 10 - 1; i++) {
  pagination += `
    <li><span class ="page-link">${i}</span></li>
`;
}

$paginationList.append(pagination);
// click on pagination num
// pass into display range
// calc and show range
$('body').on('click', '.pagination__num', function () {

  hideAll();

  // get text number 1 - 5
  // get ranges for start and end
  let paginationText = Number($(this).text());
  let startFrom = paginationText * itemTotal + paginationText;
  let end = paginationText * itemTotal + paginationText + itemTotal;

  // display ranges
  displayRange(startFrom, end);

});
$submissionSearch.addEventListener('keyup', function () {

  hideAll();

  $submissions.each(function () {
    $(this).removeClass("result");

  });


  // value of searched
  var text = $(this).val().toLowerCase();
  // results of search
  var results = $("ul.student-list li:contains('" + text.toLowerCase() + "')");

  results.addClass("result");


  // if student has result class
  // dispaly
  // else hide


  if ($submissions.hasClass('result')) {
    $('.result').show();
    $submissions.removeClass('result');

  }


});

$submissionSearch.addEventListener(function () {
  if (!this.value) {
    hideAll();
    displayRange(0, itemTotal);
  }

});

$(document).ready(function () {
  const tabs = $('.tab').click(function () {
    if (this.id == 'all') {
      $('.student-item').fadeIn(450);
    } else {
      this.classList.add('active');
      tabs.not(this).removeClass('active');
      const el = $('.' + this.id).fadeIn(450);
      $('.student-item').not(el).hide();
    }
  });
});
// !SECTION

// SECTION - JQUERY AJAX Post Request to update
function ntfy(cb) {
  alert('Submission Marked as Reviewed')
  console.info('Getting Ready to Reload Page')
  setTimeout(reloadPage(), 500000);
};
function reloadPage(){
    document.location.reload()
    setTimeout(document.location.reload(), 3000)

}
function SuccessfulUpdate(){
  notifications.snackbar('Submission Marked as Reviewed');
  
}

function markSubmissionAsReviewed(pk, cb) {
  let data = {
    "pk": pk
  }
  data = JSON.stringify(data)
  $.ajax({
    url: '/reviewed',
    data: data,
    type: 'POST',
    success: ntfy()
  });
};

// !SECTION 

// SECTION - SNACKBAR Notification

