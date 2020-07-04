var App = (function () {

    var self = this;

    self.initKatex = function () {
        $("script[type='math/tex']").replaceWith(
            function () {
                var tex = $(this).text();

                return "<span class=\"inline-equation\">" + katex.renderToString(tex) + "</span>";
            }
        );

        $("script[type='math/tex; mode=display']").replaceWith(
            function () {
                var tex = $(this).text();

                return "<div class=\"equation\">" + katex.renderToString("\\displaystyle " + tex) + "</div>";
            }
        );
    };

    self.initNavBar = function() {
        $(document).ready(function () {
            $('li.active').removeClass('active');
            console.log(location.pathname);
            $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
        });
    };


    self.init = function () {
        self.initKatex();
        self.initNavBar();
    };

    return {
        init: self.init
    };

})();



$(document).ready(function () {
    App.init();
});

