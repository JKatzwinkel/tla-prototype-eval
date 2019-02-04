$(window).on('pageshow', init);

function init() {	
// Show/Hide - Buttons
	// .hieroglyph
		$('html').not('.hieroglyph').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.hieroglyph').is(':visible') && !e.target == '.hieroglyph') {
                $('.hieroglyph').slideUp('ease-out');
            }
        });
        $('.hieroglyph-btn').click(function (e) {
			e.preventDefault();
            $('.hieroglyph').slideToggle('slow');
        });	
		
	// .translation-languages
		$('html').not('.translation-languages').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.translation-languages').is(':visible') && !e.target == '.translation-languages') {
                $('.translation-languages').slideUp('ease-out');
            }
        });

        $('.translation-languages-btn').click(function (e) {
			e.preventDefault();
            $('.translation-languages').slideToggle('slow');
        });	
	
	// .word-class
		$('html').not('.word-class').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.word-class').is(':visible') && !e.target == '.word-class') {
                $('.word-class').slideUp('ease-out');
            }
        });
        $('.word-class-btn').click(function (e) {
			e.preventDefault();
            $('.word-class').slideToggle('slow');
        });	
		
	// .combination-search
		$('html').not('.combination-search').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.combination-search').is(':visible') && !e.target == '.combination-search') {
                $('.combination-search').slideUp('ease-out');
            }
        });
        $('.combination-search-btn').click(function (e) {
			e.preventDefault();
            $('.combination-search').slideToggle('slow');
        });	
		
	// Headroom 
	    $(function() {
		var header = new Headroom(document.querySelector("#header"), {
			tolerance: 5,
			offset : 45,
			classes: {
			    // when element is initialised
				initial : "headroom",
				// when scrolling up
				pinned : "headroom--pinned",
				// when scrolling down
				unpinned : "headroom--unpinned",
				// when above offset
				top : "headroom--top"
			}
		});
		header.init();
		}());
		
		
	// scrolltop
	
		$(document).ready(function(){
			$('.show-more').on('click', function(){
				$('html,body').animate({scrollTop: $(this).offset().top}, 800);
			}); 
		}); 
	
	// change icons for show-detail-buttons
		//$(document).addEventListener('DOMContentLoaded', function () {
		$(document).ready(function() {			
			
			$('.show-detail, .show-more').click('click',function () {
				$(this)
				.find('[data-fa-i2svg]')
				.toggleClass('fas fa-plus-circle')
				.toggleClass('fas fa-minus-circle');		
			});
			/*
			$('.show-more').on('hide.bs.collapse', function () {
			  $(this)
				.find('[data-fa-i2svg]')
				.toggleClass('fas fa-minus-circle')
				.toggleClass('fas fa-plus-circle');
			});*/
			
		});
				
			
}

