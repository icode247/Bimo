$(() => {

  $('.send-feedback-form').on('submit', (event) => {
    $('.thankyou-message').html('');
    $('.your-feedback').html('');
    event.preventDefault();
    $.ajax({
      url: '/feedback/add/',
      method: 'POST',
      data: JSON.stringify({
        email: $('.email-input').val(),
        feedback: $('.feedback-input').val(),
        url: $(location).attr('href')
      }),
      headers: {'X-CSRFToken': generated_csrf_token},
    })
    .done(() => {
      toggleModal('Thank You!', null);
    })
    .fail(() => {
      toggleModal('Something went wrong.<br>Please email your feedback to us.');
    });
  });

});

function toggleModal(message) {
  $('#feedbackModal').modal('hide');
  $('#thankyouModal').modal('show');
  $('.email-input').val('');
  $('.feedback-input').val('');
  $('.thankyou-message').html(message);
}
