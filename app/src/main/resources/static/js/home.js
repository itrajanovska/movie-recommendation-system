$(document).ready(function () {
    console.log('ready');
    var pageSize = 20;

    $('#select-container').select2({
        ajax: {
            url: "/api/movies",
            dataType: 'json',
            delay: 250,
            width: 'resolve',
            data: function (params) {
                return {
                    searchTerm: params.term || '', // search term
                    page: params.page || 0,
                    size: pageSize
                };
            },
            processResults: function (data, params) {
                params.page = params.page || 0;

                return {
                    results: data.content.map(function (it) {
                        return {id: it.id, text: it.name};
                    }),
                    pagination: {
                        more: (params.page * pageSize) < data.totalElements
                    }
                };
            },
            cache: true
        },
        placeholder: 'Search for a movie'
    });

    $('#get-recommendations').click(function () {
        $.ajax({
            url: '/api/getRecommendations',
            data: {
                referenceMovies: $('#select-container').select2('data').map(function (it) {
                    return it.text;
                })
            },
            success: function (recommendedMovies) {
                displayRecommendedMovies(recommendedMovies);
            }
        })
    });

    function displayRecommendedMovies(recommendedMovies) {
        var $recommendations = $('#recommendations');
        $recommendations.empty();

        for (var i = 0; i < recommendedMovies.length; i++) {
            var $div = $("<div>", {text: recommendedMovies[i]});
            $recommendations.append($div);
        }
    }
});