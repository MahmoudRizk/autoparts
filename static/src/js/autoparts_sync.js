odoo.define('autoparts.sync', function(require) {

var ajax = require('web.ajax');
var rpc = require('web.rpc');

var category_id='';

    $(document).ready(function () {
        $("button.sync_button").on('click', function(o) {
              var my_search = $("input[name='search']")

              rpc.query({
                model: 'autoparts.autoparts',
                method: 'test_search',
                args: [{
                    'product': my_search[0].value,
                    'category': my_search[1].value,
                }]
              }).then(function (returned_value) {
                    console.log(returned_value);
                    window.location = '/shop?&category=' + returned_value['category_id'] + '&search=' + returned_value['product'];
                  });
        });
    });
});
