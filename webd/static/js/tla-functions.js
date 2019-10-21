$(window).on('pageshow', init);


function copyStringToClipboard (str) {
       // Create new element
       var el = document.createElement('textarea');
       // Set value (string to be copied)
       el.value = str;
       // Set non-editable to avoid focus and move outside of view
       el.setAttribute('readonly', '');
       el.style = {position: 'absolute', left: '-9999px'};
       document.body.appendChild(el);
       // Select text inside element
       el.select();
       // Copy text to clipboard
       document.execCommand('copy');
       // Remove temporary element
       document.body.removeChild(el);
    }
	


function init() {	
// Show/Hide - Buttons
    
    // .sidebar
		$('html').not('#sidebar').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('#sidebar').is(':visible') && !e.target == '#sidebar') {
                $('#sidebar').slideUp('ease-out');
            }
        });
        $('.sidebar-btn, .close-sidebar').click(function (e) {
			e.preventDefault();
            $('#sidebar').slideToggle('slow');
        });	
    
    
     // .hieroglyph
		/*$('html').not('.hieroglyph').click(function (e) {		       
		 if ($('.hieroglyph').is(':visible') && !e.target == '.hieroglyph') {
                $('.hieroglyph').slideUp('ease-out');
            }             
        });*/
        $('.hieroglyph-btn').click(function () {			
            //$('.hieroglyph').slideToggle('slow');
            $('.hieroglyph').toggleClass('hide show'); 
            
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

	// .result-list-attestation-time
		$('html').not('.result-list-attestation-time').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.result-list-attestation-time').is(':visible') && !e.target == '.result-list-attestation-time') {
                $('.result-list-attestation-time').slideUp('ease-out');
            }
        });
        $('.attestation-time-btn').click(function (e) {
			e.preventDefault();
            $('.result-list-attestation-time').slideToggle('slow');
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
		
  	// .flexcode (TLA flexcode)
		$('html').not('.flexcode').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.flexcode').is(':visible') && !e.target == '.flexcode') {
                $('.flexcode').slideUp('ease-out');
            }
        });
        $('.flexcode-btn').click(function (e) {
			e.preventDefault();
            $('.flexcode').slideToggle('slow');
        });	
		
  	// .ling-glossing
		$('html').not('.ling-glossing').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.ling-glossing').is(':visible') && !e.target == '.ling-glossing') {
                $('.ling-glossing').slideUp('ease-out');
            }
        });
        $('.ling-glossing-btn').click(function (e) {
			e.preventDefault();
            $('.ling-glossing').slideToggle('slow');
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
            /*$('.translation-en').slideUp('ease-out');
            $('.translation-fr').slideUp('ease-out');*/
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
            /*$('.translation-de').slideUp('ease-out');
            $('.translation-fr').slideUp('ease-out');*/
            
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
            /*$('.translation-en').slideUp('ease-out');
            $('.translation-de').slideUp('ease-out');*/
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
    
     // .corpus-path
		$('html').not('.corpus-path-all').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.corpus-path-all').is(':visible') && !e.target == '.corpus-path-all') {
                $('.corpus-path-all').slideUp('ease-out');
            }
        });
        $('.show-corpus-path').click(function (e) {
			e.preventDefault();
            $('.corpus-path-all, .hide-dots').slideToggle('slow');
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
    
    // Indented Annotation-Buttons
        $('html').not('.anno-block-btn').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.indented-buttons-annotation').is(':visible') && !e.target == '.indented-buttons-annotation') {
                $('.indented-buttons-annotation').slideUp('ease-out');
            }
        });
        $('.anno-block-btn').click(function (e) {
			e.preventDefault();
            $('.indented-buttons-annotation').slideToggle('slow');
        });
    
    // Indented Lanuage-Buttons
        $('html').not('.languages-btn').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('.indented-buttons-lang').is(':visible') && !e.target == '.indented-buttons-lang') {
                $('.indented-buttons-lang').slideUp('ease-out');
            }
        });
        $('.languages-btn').click(function (e) {
			e.preventDefault();
            $('.indented-buttons-lang').slideToggle('slow');
        });
    
	// Show/Hide Comments
        
            $('.show-comment-button').click(function()  {    
             $('.comment-wrapper').toggleClass('hide-comment show-comment');             
            $('.show-comment-button').addClass('d-none');            
            $('.hide-comment-button').removeClass('d-none');
            
            });
        
    $('.hide-comment-button').click(function()  {
           $('.comment-wrapper').toggleClass('hide-comment show-comment');            
            $('.hide-comment-button').addClass('d-none');
            $('.show-comment-button').removeClass('d-none');
            });
        
    // Cookie Alert ausblenden
    $('.cookie-ok').click(function()  {
           $('.cookie-container').addClass('d-none');
            
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
		
		
	// change button-icons
	
    $(document).ready(function() {			
        $('.show-detail').click(function() {
    
        $("i", this).toggleClass("fas fa-plus-circle fas fa-minus-circle");
            });        	
			
		}); 
     
    // scrolltop
	
		$(document).ready(function(){
			$('.show-more').on('click', function(){
				$('html,body').animate({scrollTop: $(this).offset().top}, 800);
			}); 
		}); 

}

