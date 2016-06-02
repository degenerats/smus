class @Table
  constructor: (opt) ->
    @table = opt.table

class @AttendanceTable extends @Table

  showOnlyPercents: (checkbox) ->
    @percent_checkbox = checkbox
    if @percent_checkbox.checked
      @table.bootstrapTable('showColumn', 'attendance_all_subjects')
    else
      @table.bootstrapTable('hideColumn', 'attendance_all_subjects')

  refreshTable: ()->
    @table.bootstrapTable('destroy')
    @table.bootstrapTable()
    @table.bootstrapTable('hideColumn', 'attendance_all_subjects')
    if @percent_checkbox
      @percent_checkbox.checked = false

class @ProgressTable extends @Table
  refreshTable: ()->
    @table.bootstrapTable('destroy')
    @table.bootstrapTable()
