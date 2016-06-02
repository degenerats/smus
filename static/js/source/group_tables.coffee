class @Table
  constructor: (opt) ->
    @table = opt.table

  refreshTable: () ->
    @table.bootstrapTable('destroy')
    @table.bootstrapTable()

class @AttendanceTable extends @Table

  showOnlyPercents: (checkbox) ->
    @percent_checkbox = checkbox
    if @percent_checkbox.checked
      @table.bootstrapTable('showColumn', 'attendance_all_subjects')
    else
      @table.bootstrapTable('hideColumn', 'attendance_all_subjects')

  refreshTable: () ->
    @table.bootstrapTable('destroy')
    @table.bootstrapTable()
    @table.bootstrapTable('hideColumn', 'attendance_all_subjects')
    if @percent_checkbox
      @percent_checkbox.checked = false

class @WorkTable extends @Table
  sortByProgress: (a, b) ->
    a = +$(a).find('.progress-bar').attr('aria-valuenow')
    b = +$(b).find('.progress-bar').attr('aria-valuenow')
    if a > b then return 1
    if a < b then return -1
    0
