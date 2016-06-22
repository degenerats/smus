class @Table
  constructor: (opt) ->
    @table = opt.table
    @params = {}

  refreshTable: () ->
    @table.bootstrapTable('destroy')
    @table.bootstrapTable()

  refreshTopControls: () ->
    try
      @table.parents('.tab-pane').find('.top-controls').find('[name="subject"]').selectpicker 'refresh'
    catch
    try
      @table.parents('.tab-pane').find('.top-controls').find('[name="semester"]').selectpicker 'refresh'
    catch

  filterBySemester: (select) ->
    @ajaxRequest $(select).serialize(), true

  getParams: (request_params, is_remove) ->
    if is_remove
      @params = {}

    new_params = $.getQueryParameters request_params

    if !request_params
      if @params.hasOwnProperty 'subject'
        delete @params.subject
      if new_params.hasOwnProperty 'subject'
        delete @params.subject

    $.param $.extend(@params, new_params)

  ajaxRequest: (params, is_semester_select = false) ->
    self = @
    request_params = @getParams params, is_semester_select

    $.ajax @current_url,
      data: request_params,
      beforeSend: =>
        @table.bootstrapTable 'showLoading'
      complete: (xhr, status) ->
        self.table.bootstrapTable()
      success: (data) =>
        table_new = $(data).find("##{@table.attr('id')}")
        @table.bootstrapTable('destroy')
        @table.html table_new.html()
        @table.parents('.tab-pane').find('.top-controls').replaceWith(table_new.parents('.tab-pane').find('.top-controls'))
        @refreshTopControls()

class @AttendanceTable extends @Table

  showOnlyPercents: (checkbox) ->
    $('.fixed-table-header-columns').remove() # fix duplicated
    $('.fixed-table-body-columns').remove() # fix duplicated
    @percent_checkbox = checkbox
    if @percent_checkbox.checked
      @table.bootstrapTable('showColumn', 'attendance_all_subjects')
    else
      @table.bootstrapTable('hideColumn', 'attendance_all_subjects')

  refreshTable: () ->
    @table.bootstrapTable('destroy')
    @table.bootstrapTable()
    if @percent_checkbox
      @percent_checkbox.checked = false
    if @select_subject
      @select_subject.selectpicker('val', 'all')

  filterBySubject: (select) ->
    if select.value != 'all'
      @ajaxRequest $(select).serialize()
    else
      @ajaxRequest null

  filterByDate: (datepicker) ->
    @ajaxRequest $(datepicker).serialize()

  initDatePicker: (selector) ->
    @datepicker = $(selector)

    @datepicker.datepicker
        language: 'ru'
        # startDate: ->
        #   console.log @.data('start-value')
        #   @.data('start-value')
        # endDate: ->
        #   console.log @.data('end-value')
        #   @.data('end-value')

  listenOnChangeDate: () ->
    @datepicker.on 'changeDate', () =>
      @filterByDate(@)

class @WorkTable extends @Table
  sortByProgress: (a, b) ->
    a = +$(a).find('.progress-bar').attr('aria-valuenow')
    b = +$(b).find('.progress-bar').attr('aria-valuenow')
    if a > b then return 1
    if a < b then return -1
    0
