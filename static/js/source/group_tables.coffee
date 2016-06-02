class @Table
  constructor: (opt) ->
    @table = opt.table

class @AttendanceTable extends @Table

  showOnlyPercents: ->
    @table.bootstrapTable('hideColumn', 'attendance_all_subjects')
