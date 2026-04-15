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

// Add to card functionality
$(document).on('click','#Addtocart',function(){
    $.ajax({
        "type":"POST",
        // "url":"{% url '' %}"
    })
});