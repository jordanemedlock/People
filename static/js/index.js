$(function() {
    if ($('#personality-graph').is(':visible')) {
        $('#personality-graph').spiderplot({
            names: _.keys(person.personality),
            values: _.values(person.personality)
        })
    }


})
