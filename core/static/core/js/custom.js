document.addEventListener("DOMContentLoaded", function () {
    let lazyImages = document.querySelectorAll(".lazy");
    let observer = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                let img = entry.target;
                img.src = img.dataset.src;
                img.onload = () => {
                    img.classList.add("loaded");
                };
                observer.unobserve(img);
            }
        });
    });
    lazyImages.forEach(img => {
        observer.observe(img);
    });
});

function switchImage(el) {
    document.getElementById("mainImage").src = el.src;
}

// Quantity button plus and minus (product-detail)
$(document).on('click', '.plus', function () {
    let qty = parseInt($('#quantity').val());
    $('#quantity').val(qty + 1);
});
$(document).on('click', '.minus', function () {
    let qty = parseInt($('#quantity').val());
    if (qty > 1) {
        $('#quantity').val(qty - 1);
    }
});
// Quantity button plus and minus (cart-overview)
$(document).on('click', '.plus', function () {
    let id = $(this).data('id');
    let input = $('.quantity-input[data-id="' + id + '"]');
    let qty = parseInt(input.val());
    input.val(qty + 1);
});
$(document).on('click', '.minus', function () {
    let id = $(this).data('id');
    let input = $('.quantity-input[data-id="' + id + '"]');
    let qty = parseInt(input.val());
    if (qty > 1) {
        input.val(qty - 1);
    }
});
// custom toastr
    function showToast(message, type = 'success') {
        let toast = $('#toast');
        if (!toast.length) {
            $('body').append(`
                <div id="toast" class="toast-success" style="display:none;">
                    <span id="toast-message"></span>
                    <span class="toast-close">&times;</span>
                </div>
            `);
            toast = $('#toast');
        }
        toast.removeClass('toast-success toast-error')
            .addClass(type === 'error' ? 'toast-error' : 'toast-success');
        $('#toast-message').text(message);
        toast.show();
        setTimeout(function () {
            toast.hide();
        }, 5000);
        $('#timelineDrawer').removeClass('open');
        $('body').removeClass('drawer-open');
    }