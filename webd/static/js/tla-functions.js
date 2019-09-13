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
		
	// .result-list-lemma-id
		$('html').not('.result-list-lemma-id').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.result-list-lemma-id').is(':visible') && !e.target == '.result-list-lemma-id') {
                $('.result-list-lemma-id').slideUp('ease-out');
            }
        });
        $('.lemma-id-btn').click(function (e) {
			e.preventDefault();
            $('.result-list-lemma-id').slideToggle('slow');
        });	

	// .result-list-bibliography
		$('html').not('.result-list-bibliography').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.result-list-bibliography').is(':visible') && !e.target == '.result-list-bibliography') {
                $('.result-list-bibliography').slideUp('ease-out');
            }
        });
        $('.bibliografical-btn').click(function (e) {
			e.preventDefault();
            $('.result-list-bibliography').slideToggle('slow');
        });	
	
	// .lemma-id
		$('html').not('.lemma-id').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.lemma-id').is(':visible') && !e.target == '.lemma-id') {
                $('.lemma-id').slideUp('ease-out');
            }
        });
        $('.lemma-id-btn').click(function (e) {
			e.preventDefault();
            $('.lemma-id').slideToggle('slow');
        });	

 	// .word-id
		$('html').not('.word-id').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.word-id').is(':visible') && !e.target == '.word-id') {
                $('.word-id').slideUp('ease-out');
            }
        });
        $('.word-id-btn').click(function (e) {
			e.preventDefault();
            $('.word-id').slideToggle('slow');
        });	

 	// .part-of-speech
		$('html').not('.part-of-speech').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.part-of-speech').is(':visible') && !e.target == '.part-of-speech') {
                $('.part-of-speech').slideUp('ease-out');
            }
        });
        $('.part-of-speech-btn').click(function (e) {
			e.preventDefault();
            $('.part-of-speech').slideToggle('slow');
        });	
		
  	// .glossing
		$('html').not('.glossing').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.glossing').is(':visible') && !e.target == '.glossing') {
                $('.glossing').slideUp('ease-out');
            }
        });
        $('.glossing-btn').click(function (e) {
			e.preventDefault();
            $('.glossing').slideToggle('slow');
        });	
		
   // Translation Languages
	// .translation-languages DE
		$('html').not('.translation-languages-btn-de').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.translation-de').is(':visible') && !e.target == '.translation-de') {
                $('.translation-de').slideUp('ease-out');
            }
        });

        $('.translation-languages-btn-de').click(function (e) {
			e.preventDefault();
            $('.translation-de').slideToggle('slow');
        });	
    
    // .translation-languages EN
		$('html').not('.translation-languages-btn-en').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.translation-en').is(':visible') && !e.target == '.translation-en') {
                $('.translation-en').slideUp('ease-out');
            }
        });

        $('.translation-languages-btn-en').click(function (e) {
			e.preventDefault();
            $('.translation-en').slideToggle('slow');
        });	
    
    // .translation-languages FR
		$('html').not('.translation-languages-btn-fr').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.translation-fr').is(':visible') && !e.target == '.translation-fr') {
                $('.translation-fr').slideUp('ease-out');
            }
        });

        $('.translation-languages-btn-fr').click(function (e) {
			e.preventDefault();
            $('.translation-fr').slideToggle('slow');
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
    
        
    // .anno-block-btn
		$('html').not('.anno-block-btn').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.container-annotation-switch').is(':visible') && !e.target == '.container-annotation-switch') {
                $('.container-annotation-switch').slideUp('ease-out');
            }
        });
        $('.anno-block-btn').click(function (e) {
			e.preventDefault();
            $('.container-annotation-switch').slideToggle('slow');
        });	
    
    
	// Copy-Text-Button
    
   // muss noch geschrieben werden
    
    
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
				let button = $(this);
				// change icons for show-detail-buttons
				$("[aria-expanded^=true]").each(function() {
					$(this)
						.find("[data-fa-i2svg]")
						.removeClass("fa-minus-circle")
						.addClass("fa-plus-circle");
				});
				$('html,body').animate({scrollTop: $(this).offset().top}, 800);
				if (button.is("[aria-expanded^=false]")) {
					$(this)
						.find('[data-fa-i2svg]')
						.removeClass('fa-plus-circle')
						.addClass('fa-minus-circle');
					$("#submit-search-form").attr(
						"form",
						$(this).attr("form")
					);
				}
			}); 
		}); 
	
}

