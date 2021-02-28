Sub VBAHW():
    
    Dim countrow As Double
    Dim countcol As Integer
    Dim counter As Double
    Dim p_open As Double
    Dim p_close As Double
    Dim vol As Double
    Dim op_col As Integer
    Dim cl_col As Integer
    Dim vol_col As Integer
    Dim y_col As Integer
    Dim year_cell As String
    Dim ws As Worksheet
    Dim nf As String
    
    nf = "N/A"
    
    y_col = 2

    op_col = 3

    cl_col = 6

    vol_col = 7
       
    Sheets.Add.Name = "sumdog"

    Sheets("sumdog").Move Before:=Sheets(1)
    
    Set combined_sheet = Worksheets("sumdog")

    counter = 1
    
    For Each ws In Worksheets
    
        If ws.Name = "2016" Then
        
        countrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        countcol = ws.Cells(1, Columns.Count).End(xlToLeft).Column
        
            For i = 1 To countrow
                
                If i = 1 Then
            
                    combined_sheet.Cells(1, 1).Value = ws.Cells(i, 1).Value
            
                    counter = counter + 1
               
                ElseIf ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            
                    counter = counter + 1
                
                    combined_sheet.Cells((counter - 1), 1).Value = ws.Cells(i, 1).Value
                
                End If
            
            Next i
            counter = counter - 1
        
        End If
                    
    Next ws
    
    counter = 2
    
    sum_col_count = 2

    For Each ws In Worksheets
        
        If ws.Name <> "sumdog" Then
        
            countrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
            
            countcol = ws.Cells(1, Columns.Count).End(xlToLeft).Column
            
            p_open = ws.Cells(2, op_col).Value
               
            volume = 0

            year_cell = ws.Name
                                
            combined_sheet.Cells(1, sum_col_count + 1).Value = year_cell + " Yearly Change"
            
            combined_sheet.Cells(1, sum_col_count + 2).Value = year_cell + " % Yearly Change"
            
            combined_sheet.Cells(1, sum_col_count) = year_cell + " Volume"

                For i = 2 To countrow + 1
    
                    'if the iteration through the sheets ticker is equal to the combined sheet ticker, go through the first hit columnwise and pull the open then keep going until
                    'the year column's first four digits change, take those first four digits, make it the name for cells(1, j) pull the close date for the i - 1, and pull the
                    'open date for the current row you are on. all the while every row you go through, you need to tally volume up to be printed into the corresponding cell for each year.
    
                    
                     ' if the next rows ticker is the !!different!!, print the volume value into the summary table and reset it. also grab this rows close value, and next rows open value and print them
                    If combined_sheet.Cells(counter, 1).Value = ws.Cells(i, 1).Value And ws.Cells(i + 1, 1).Value <> combined_sheet.Cells(counter, 1).Value Then
    
                        p_close = ws.Cells(i, cl_col).Value
    
                        combined_sheet.Cells(counter, sum_col_count + 1).Value = p_open - p_close
                        
                        If p_open = 0 Then
                            
                            combined_sheet.Cells(counter, sum_col_count + 2).Value = nf
                            
                            p_open = ws.Cells(i + 1, op_col).Value
        
                            'sum_col_count = sum_col_count + 2
                        
                        Else
                          
                            combined_sheet.Cells(counter, sum_col_count + 2).Value = CDbl((p_close - p_open) / p_open)
        
                            p_open = ws.Cells(i + 1, op_col).Value
        
                            'sum_col_count = sum_col_count + 2
                        
                        End If
                        
                    ElseIf ws.Cells(i, 1).Value = combined_sheet.Cells(counter, 1).Value Then
                        
                         'adds volume up while iterating through same ticker
                        volume = volume + ws.Cells(i, vol_col).Value
                    
    
                    ElseIf combined_sheet.Cells(counter, 1).Value <> ws.Cells(i, 1).Value Then
    
                        combined_sheet.Cells(counter, sum_col_count) = volume
    
                        volume = 0
    
                        counter = counter + 1

                    End If
                    
                Next i

            sum_col_count = sum_col_count + 3
            
            counter = 2

        End If

    Next ws
    countrow = combined_sheet.Cells(Rows.Count, 1).End(xlUp).Row

    Dim MyRange As Range

    Set MyRange = combined_sheet.Range("C2" & ":D" & countrow & "," & "F2" & ":G" & countrow & "," & "I2" & ":J" & countrow)

    MyRange.FormatConditions.Delete

    MyRange.FormatConditions.Add Type:=xlCellValue, Operator:=xlLess, _
            Formula1:="=0"
    MyRange.FormatConditions(1).Interior.Color = RGB(255, 0, 0)
    
    MyRange.FormatConditions.Add Type:=xlCellValue, Operator:=xlGreater, _
            Formula1:="=0"
    MyRange.FormatConditions(2).Interior.Color = RGB(0, 255, 0)
    
End Sub

