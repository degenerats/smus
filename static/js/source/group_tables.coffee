class @Table
  constructor: (opt) ->
    @table = opt.table
    @current_url = window.location.origin + window.location.pathname

  refreshTable: () ->
    @table.bootstrapTable('destroy')
    @table.bootstrapTable()

  updateUrl: (url) ->
    history.pushState
      url: url

  getParams: (request_params) ->
    current_params = $.getQueryParameters window.location.search
    new_params = $.getQueryParameters request_params
    $.param $.extend(current_params, new_params)

  ajaxRequest: (params) ->
    self = @
    request_params = @getParams params

    $.ajax @current_url,
      data: request_params,
      beforeSend: =>
        @table.bootstrapTable 'showLoading'
      complete: (xhr, status) ->
        self.table.bootstrapTable()
        if status == 'success'
          history.replaceState null, null, @.url
      success: (data) =>
        @table.bootstrapTable('destroy')
        @table.html($(data).find("##{@table.attr('id')}").html())


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
    @table.bootstrapTable('hideColumn', 'attendance_all_subjects')
    if @percent_checkbox
      @percent_checkbox.checked = false
    if @select_subject
      @select_subject.selectpicker('val', 'all')

  filterBySubject: (select) ->
    if select.value != 'all'
      @ajaxRequest $(select).serialize()
    else
      window.location.search = window.location.search.replace(/&?subject=([^&]$|[^&]*)/i, "")

  filterByDate: (select) ->
    # AJAX call here and table update

  filterBySemester: (select) ->
    # AJAX call here and table update


class @WorkTable extends @Table
  sortByProgress: (a, b) ->
    a = +$(a).find('.progress-bar').attr('aria-valuenow')
    b = +$(b).find('.progress-bar').attr('aria-valuenow')
    if a > b then return 1
    if a < b then return -1
    0
