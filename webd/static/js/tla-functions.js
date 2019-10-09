$(window).on('pageshow', init);


// Sidebar 
 /*   $('html').not('#sidebar').click(function (e) {
		        //console.log($(e.target).parent());
		 if ($('#sidebar').is(':visible') && !e.target == '#sidebar') {
                $('#sidebar').toggle('slide', 
                    {direction: 'right'}, 
                    500);
            }
        });

    $('.sandwich').click(function (e) {
			e.preventDefault();
            $('#sidebar').toggle('fast');
        });
    $('.close-sidebar').click(function (e) {
			e.preventDefault();
            $('#sidebar').toggle('fast');
        });
*/


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
	
function getCookie(Bezeichner) {
  var Wert = "";
  if (document.cookie) {
    var Wertstart = document.cookie.indexOf(Bezeichner+"=") + Bezeichner.length +1;
    var Wertende = document.cookie.indexOf(";", Wertstart);
    if (Wertende < Wertstart) {
      Wertende = document.cookie.length;
	}
	Wert = document.cookie.substring(Wertstart, Wertende);
  }
  return Wert;
}

function setCookie(Bezeichner, Wert) {
  var jetzt = new Date();
  var Auszeit = new Date(jetzt.getTime() + 1000 * 60 * 60 * 24 * 365);
  document.cookie = Bezeichner + "=" + Wert + "; expires=" + Auszeit.toGMTString() + "; path=/; samesite=lax";
}

function init() {	

    // Cookie Acceptance Banner ausblenden

	  var cookieAcceptanceState = getCookie("CookiePolicy");
	  if (cookieAcceptanceState == "accepted") {
		  $('.cookie-container').addClass('d-none');
		  var ausgabe = document.getElementById('info');
		  ausgabe.innerHTML = '(Cookie '+cookieAcceptanceState+')';
	  }
	
    $('.cookie-ok').click(function()  {
           $('.cookie-container').addClass('d-none');
            setCookie("CookiePolicy", "accepted");
            });
		
    $('.cookie-dismissed').click(function()  {
           $('.cookie-container').addClass('d-none');
            });

	// Search-Button
	
    $('.dictionary-search-form-btn').click(function()  {
		  var search_btn = document.getElementById("submit-search-form");
		  search_btn.innerHTML = '<span class="fas fa-arrow-circle-right"></span>Search in dictionary';
		  search_btn.setAttribute('form','dict-search')
		  });	

    $('.text-word-search-form-btn').click(function()  {
		  var search_btn = document.getElementById("submit-search-form");
		  search_btn.innerHTML = '<span class="fas fa-arrow-circle-right"></span>Search in texts';
		  search_btn.setAttribute('form','text-word-search')
		  });	

			
	// Show/Hide - Buttons
    
		// .sidebar
		$('html').not('#sidebar').click(function (e) {
		 if ($('#sidebar').is(':visible') && !e.target == '#sidebar') {
                $('#sidebar').slideUp('ease-out');
            }
        });
        $('.sidebar-btn, .close-sidebar').click(function (e) {
			e.preventDefault();
            $('#sidebar').slideToggle('slow');
        });	
    
    
		// .hieroglyph
		if (getCookie("HieroglyphsVisible") == "false") {
			$('i', '.hieroglyph-btn').addClass("fa-minus-circle")
			$('.hieroglyph').hide();
			}
		else {
			$('i', '.hieroglyph-btn').addClass("fa-plus-circle")
			$('.hieroglyph').show();
			}
			
		$('html').not('.hieroglyph').click(function (e) {
		 if ($('.hieroglyph').is(':visible') && !e.target == '.hieroglyph') {
                $('.hieroglyph').slideUp('ease-out');
            }
        });
        $('.hieroglyph-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.hieroglyph').is(':visible')) {
					setCookie("HieroglyphsVisible", "false");
				} else {
					setCookie("HieroglyphsVisible", "true");
				}
			}
            $('.hieroglyph').slideToggle('slow');
        });	
		
	// .lemma-id
		if (getCookie("LemmaIDVisible") == "true") {
			$('i', '.lemma-id-btn').addClass("fa-plus-circle")
			$('.lemma-id').show();
			}
		else {
			$('i', '.lemma-id-btn').addClass("fa-minus-circle")
			$('.lemma-id').hide();
			}

		$('html').not('.lemma-id').click(function (e) {
		 if ($('.lemma-id').is(':visible') && !e.target == '.lemma-id') {
                $('.lemma-id').slideUp('ease-out');
            }
        });
        $('.lemma-id-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.lemma-id').is(':visible')) {
					setCookie("LemmaIDVisible", "false");
				} else {
					setCookie("LemmaIDVisible", "true");
				}
			}
            $('.lemma-id').slideToggle('slow');
        });	

	// .bibliography-list
		if (getCookie("BibliographyVisible") == "true") {
			$('i', '.bibliography-list-btn').addClass("fa-plus-circle")
			$('.bibliography-list').show();
			}
		else {
			$('i', '.bibliography-list-btn').addClass("fa-minus-circle")
			$('.bibliography-list').hide();
			}

		$('html').not('.bibliography-list').click(function (e) {
		 if ($('.bibliography-list').is(':visible') && !e.target == '.bibliography-list') {
                $('.bibliography-list').slideUp('ease-out');
            }
        });
        $('.bibliography-list-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.bibliography-list').is(':visible')) {
					setCookie("BibliographyVisible", "false");
				} else {
					setCookie("BibliographyVisible", "true");
				}
			}
            $('.bibliography-list').slideToggle('slow');
        });	

	// .attestation-time
		if (getCookie("AttestationTimeVisible") == "true") {
			$('i', '.attestation-time-btn').addClass("fa-plus-circle")
			$('.attestation-time').show();
			}
		else {
			$('i', '.attestation-time-btn').addClass("fa-minus-circle")
			$('.attestation-time').hide();
			}

		$('html').not('.attestation-time').click(function (e) {
		 if ($('.attestation-time').is(':visible') && !e.target == '.attestation-time') {
                $('.attestation-time').slideUp('ease-out');
            }
        });
        $('.attestation-time-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.attestation-time').is(':visible')) {
					setCookie("AttestationTimeVisible", "false");
				} else {
					setCookie("AttestationTimeVisible", "true");
				}
			}
            $('.attestation-time').slideToggle('slow');
        });	

 	// .word-id
		if (getCookie("WordIDVisible") == "true") {
			$('i', '.word-id-btn').addClass("fa-plus-circle")
			$('.word-id').show();
			}
		else {
			$('i', '.word-id-btn').addClass("fa-minus-circle")
			$('.word-id').hide();
			}

		$('html').not('.word-id').click(function (e) {
		 if ($('.word-id').is(':visible') && !e.target == '.word-id') {
                $('.word-id').slideUp('ease-out');
            }
        });
        $('.word-id-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.word-id').is(':visible')) {
					setCookie("WordIDVisible", "false");
				} else {
					setCookie("WordIDVisible", "true");
				}
			}
            $('.word-id').slideToggle('slow');
        });	

	// .word-class
		if (getCookie("WordClassVisible") == "true") {
			$('i', '.word-class-btn').addClass("fa-plus-circle")
			$('.word-class').show();
			}
		else {
			$('i', '.word-class-btn').addClass("fa-minus-circle")
			$('.word-class').hide();
		}

		$('html').not('.word-class').click(function (e) {
		 if ($('.word-class').is(':visible') && !e.target == '.word-class') {
                $('.word-class').slideUp('ease-out');
            }
        });
        $('.word-class-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.word-class').is(':visible')) {
					setCookie("WordClassVisible", "false");
				} else {
					setCookie("WordClassVisible", "true");
				}
			}
            $('.word-class').slideToggle('slow');
        });	
		
  	// .flexcode (TLA flexcode)
		if (getCookie("TLAFlexcodeVisible") == "true") {
			$('i', '.flexcode-btn').addClass("fa-plus-circle")
			$('.flexcode').show();
			}
		else {
			$('i', '.flexcode-btn').addClass("fa-minus-circle")
			$('.flexcode').hide();
			}

		$('html').not('.flexcode').click(function (e) {
		 if ($('.flexcode').is(':visible') && !e.target == '.flexcode') {
                $('.flexcode').slideUp('ease-out');
            }
        });
        $('.flexcode-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.flexcode').is(':visible')) {
					setCookie("TLAFlexcodeVisible", "false");
				} else {
					setCookie("TLAFlexcodeVisible", "true");
				}
			}
            $('.flexcode').slideToggle('slow');
        });	
		
  	// .ling-glossing
		if (getCookie("LingGlossingVisible") == "true") {
			$('i', '.ling-glossing-btn').addClass("fa-plus-circle")
			$('.ling-glossing').show();
			}
		else {
			$('i', '.ling-glossing-btn').addClass("fa-minus-circle")
			$('.ling-glossing').hide();
			}

		$('html').not('.ling-glossing').click(function (e) {
		 if ($('.ling-glossing').is(':visible') && !e.target == '.ling-glossing') {
                $('.ling-glossing').slideUp('ease-out');
            }
        });
        $('.ling-glossing-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.ling-glossing').is(':visible')) {
					setCookie("LingGlossingVisible", "false");
				} else {
					setCookie("LingGlossingVisible", "true");
				}
			}
            $('.ling-glossing').slideToggle('slow');
        });	
		
   // Translation Languages
   
    // Indented Language-Buttons
		if (getCookie("LanguagesButtonsVisible") == "true") {
			$('.indented-buttons-lang').show();
			}
		else {
			$('.indented-buttons-lang').hide();
			}

        $('html').not('.languages-btn').click(function (e) {
		 if ($('.indented-buttons-lang').is(':visible') && !e.target == '.indented-buttons-lang') {
                $('.indented-buttons-lang').slideUp('ease-out');
            }
        });
        $('.languages-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.indented-buttons-lang').is(':visible')) {
					setCookie("LanguagesButtonsVisible", "false");
				} else {
					setCookie("LanguagesButtonsVisible", "true");
				}
			}
            $('.indented-buttons-lang').slideToggle('slow');
        });
		
		
	// .translation-languages DE
		if (getCookie("TranslationDEVisible") == "false") {
			$('i', '.translation-de-btn').addClass("fa-minus-circle")
			$('.translation-de').hide();
			}
		else {
			$('i', '.translation-de-btn').addClass("fa-plus-circle")
			$('.translation-de').show();
			}

		$('html').not('.translation-de').click(function (e) {
		 if ($('.translation-de').is(':visible') && !e.target == '.translation-de') {
                $('.translation-de').slideUp('ease-out');                
            }
        });
        $('.translation-de-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.translation-de').is(':visible')) {
					setCookie("TranslationDEVisible", "false");
				} else {
					setCookie("TranslationDEVisible", "true");
				}
			}
            $('.translation-de').slideToggle('slow');
            /*$('.translation-en').slideUp('ease-out');
            $('.translation-fr').slideUp('ease-out');*/
        });	
    
    // .translation-languages EN
		if (getCookie("TranslationENVisible") == "true") {
			$('i', '.translation-en-btn').addClass("fa-plus-circle")
			$('.translation-en').show();
			}
		else {
			$('i', '.translation-en-btn').addClass("fa-minus-circle")
			$('.translation-en').hide();
			}

		$('html').not('.translation-en').click(function (e) {
		 if ($('.translation-en').is(':visible') && !e.target == '.translation-en') {
                $('.translation-en').slideUp('ease-out');               
            }
        });

        $('.translation-en-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.translation-en').is(':visible')) {
					setCookie("TranslationENVisible", "false");
				} else {
					setCookie("TranslationENVisible", "true");
				}
			}
            $('.translation-en').slideToggle('slow');
            /*$('.translation-de').slideUp('ease-out');
            $('.translation-fr').slideUp('ease-out');*/
            
        });	
    
    // .translation-languages FR
		if (getCookie("TranslationFRVisible") == "true") {
			$('i', '.translation-fr-btn').addClass("fa-plus-circle")
			$('.translation-fr').show();
			}
		else {
			$('i', '.translation-fr-btn').addClass("fa-minus-circle")
			$('.translation-fr').hide();
			}

		$('html').not('.translation-fr').click(function (e) {
		 if ($('.translation-fr').is(':visible') && !e.target == '.translation-fr') {
                $('.translation-fr').slideUp('ease-out');
            }
        });

        $('.translation-fr-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.translation-fr').is(':visible')) {
					setCookie("TranslationFRVisible", "false");
				} else {
					setCookie("TranslationFRVisible", "true");
				}
			}
            $('.translation-fr').slideToggle('slow');
            /*$('.translation-en').slideUp('ease-out');
            $('.translation-de').slideUp('ease-out');*/
        });	 
    
      
	// .combination-search
		$('html').not('.combination-search').click(function (e) {
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
		 if ($('.corpus-path-all').is(':visible') && !e.target == '.corpus-path-all') {
                $('.corpus-path-all').slideUp('ease-out');
            }
        });
        $('.show-corpus-path').click(function (e) {
			e.preventDefault();
            $('.corpus-path-all, .hide-dots').slideToggle('slow');
        });	
    
        
    // .anno-block-btn
		if (getCookie("AnnotationBlockVisible") == "true") {
			$('i', '.anno-block-btn').addClass("fa-plus-circle")
			$('.container-annotation-switch-anno').show();
			$('.container-annotation-switch-lines').hide();
			$('.indented-buttons-annotation').show();
			}
		else {
			$('i', '.anno-block-btn').addClass("fa-minus-circle")
			$('.container-annotation-switch-anno').hide();
			$('.container-annotation-switch-lines').show();
			$('.indented-buttons-annotation').hide();
			}

		$('html').not('.anno-block-btn').click(function (e) {
		 if ($('.container-annotation-switch-anno').is(':visible') && !e.target == '.container-annotation-switch-anno') {
                $('.container-annotation-switch-anno').slideUp('ease-out');
            }
		 if ($('.indented-buttons-annotation').is(':visible') && !e.target == '.indented-buttons-annotation') {
                $('.indented-buttons-annotation').slideUp('ease-out');
            }
        });
        $('.anno-block-btn').click(function (e) {
			e.preventDefault();
			if (getCookie("CookiePolicy") == "accepted") {
				if ($('.container-annotation-switch-anno').is(':visible')) {
					setCookie("AnnotationBlockVisible", "false");
				} else {
					setCookie("AnnotationBlockVisible", "true");
				}
			}
            $('.container-annotation-switch-anno').slideToggle('slow');
            $('.container-annotation-switch-lines').slideToggle('slow');
            $('.indented-buttons-annotation').slideToggle('slow');
        });	
    
    // Indented Annotation-Buttons
 /*       $('html').not('.anno-block-btn').click(function (e) {
		 if ($('.indented-buttons-annotation').is(':visible') && !e.target == '.indented-buttons-annotation') {
                $('.indented-buttons-annotation').slideUp('ease-out');
            }
        });
        $('.anno-block-btn').click(function (e) {
			e.preventDefault();
            $('.indented-buttons-annotation').slideToggle('slow');
        });*/
    
    
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

