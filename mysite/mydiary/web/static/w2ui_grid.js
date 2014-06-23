/*
* w3ui wediget demo code [javascript]
*/

$('#dataTable').w2grid({
    name: 'grid',
    header: 'List of Names',
    show: {
        toolbar: true,
        footer: true,
		toobarSave:true
    },
    columns: [
        { field: 'recid', caption: 'ID', size: '50px', sortable: true, attr: 'align=center' },
        { field: 'lname', caption: 'Last Name', size: '30%', sortable: true, resizable: true },
        { field: 'fname', caption: 'First Name', size: '30%', sortable: true, resizable: true },
        { field: 'email', caption: 'Email', size: '40%', resizable: true },
        { field: 'sdate', caption: 'Start Date', size: '120px', resizable: true },
    ],
    searches: [
        { field: 'lname', caption: 'Last Name', type: 'text' },
        { field: 'fname', caption: 'First Name', type: 'text' },
        { field: 'email', caption: 'Email', type: 'text' },
    ],
    sortData: [{ field: 'recid', direction: 'ASC' }],
    records: [
        { recid: 1, fname: 'John', lname: 'doe', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 2, fname: 'Stuart', lname: 'Motzart', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 3, fname: 'Jin', lname: 'Franson', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 4, fname: 'Susan', lname: 'Ottie', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 5, fname: 'Kelly', lname: 'Silver', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 6, fname: 'Francis', lname: 'Gatos', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 7, fname: 'Mark', lname: 'Welldo', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 8, fname: 'Thomas', lname: 'Bahh', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 9, fname: 'Sergei', lname: 'Rachmaninov', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 20, fname: 'Jill', lname: 'Doe', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 21, fname: 'Frank', lname: 'Motzart', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 22, fname: 'Peter', lname: 'Franson', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 23, fname: 'Andrew', lname: 'Ottie', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 24, fname: 'Manny', lname: 'Silver', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 25, fname: 'Ben', lname: 'Gatos', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 26, fname: 'Doer', lname: 'Welldo', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 27, fname: 'Shashi', lname: 'bahh', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
        { recid: 28, fname: 'Av', lname: 'Rachmaninov', email: 'jdoe@gmail.com', sdate: '4/3/2012' }
    ],
	toolbar: {
items: [
        { id: 'add', type: 'button', caption: 'Add', img: 'icon-add' }
          ],

            onClick: function (event) {
                  if (event.target == 'add') {
                             w2ui.grid.add({ recid: w2ui.grid.records.length + 1 });
                         }
                   }
              },
});

$('#toolbar').w2toolbar({
	name: 'toolbar',
	items: [
		{ type: 'check',  id: 'item1', caption: 'Check', img: 'icon-page', checked: true },
		{ type: 'break',  id: 'break0' },
		{ type: 'menu',   id: 'item2', caption: 'Drop Down', img: 'icon-folder', items: [
			{ text: 'Item 1', icon: 'icon-page' }, 
			{ text: 'Item 2', icon: 'icon-page' }, 
			{ text: 'Item 3', value: 'Item Three', icon: 'icon-page' }
		]},
		{ type: 'break', id: 'break1' },
		{ type: 'radio',  id: 'item3',  group: '1', caption: 'Radio 1', img: 'icon-add', checked: true },
		{ type: 'radio',  id: 'item4',  group: '1', caption: 'Radio 2', img: 'icon-add' },
		{ type: 'spacer' },
		{ type: 'button',  id: 'item5',  caption: 'Item 5', img: 'icon-save' },
		{ type: 'button',  id: 'item6',  caption: 'Item 6', img: 'icon-save' },
	]
});

$('#toolbar2').w2toolbar({
	name: 'toolbar2',
	items: [
		{ type: 'spacer' },
		{ type: 'button',  id: 'btnSave',  caption: 'OK', img: 'icon-save' },
		{ type: 'button',  id: 'btnReset',  caption: 'reset', img: 'icon-cancel' }
	]
});
