' Use Alt + F11 to Open VBA editor in Outlook
' Add Microsoft VBScript Regulare Expression 5.5 by Toos -> References
' Copy the script to the VBA editor
' Compile by Debug - > Compile xxx to make sure there is no grammar issue
' Save the VBS project and Create a email rule to run this script
' BTW: You may need to disable Macro security check by: Outlook Option -> Trust Center -> Trust Center Settings -> Macro Setting


Public Sub SaveBuildLog(item As Outlook.MailItem)
    Dim objAtt As Outlook.Attachment

    'MsgBox "processing email with subject: " & item.Subject
    'Dim sucessPos As Integer
    'sucessPos = InStr(item.subject, "succeeded")
    'If sucessPos > 0 Then
    '    Return
    'End If
    
    ' Example:
    '          MyProject-03.20_03.20.0913.000
    Dim buildNumber As String
    buildNumber = regex(item.Subject, "MyProject-\d\d.\d\d_\d\d.\d\d.\d\d\d\d.000")
    
    Dim saveFolder As String
    saveFolder = "\\file_server\daily_build\"
    
    For Each objAtt In item.Attachments
        Dim pos As Integer
        pos = InStr(objAtt.DisplayName, "build.log")

        If pos > 0 Then
            pos = InStr(objAtt.DisplayName, "build.log.zip")
            If pos > 0 Then
                objAtt.SaveAsFile saveFolder & "\" & buildNumber & "_build.log.zip"
            Else
                objAtt.SaveAsFile saveFolder & "\" & buildNumber & "_build.log"
            End If
            Set objAtt = Nothing
        End If
    Next
End Sub

Function regex(strInput As String, matchPattern As String, Optional ByVal outputPattern As String = "$0") As Variant
    
    Dim inputRegexObj As New VBScript_RegExp_55.RegExp, outputRegexObj As New VBScript_RegExp_55.RegExp, outReplaceRegexObj As New VBScript_RegExp_55.RegExp
    Dim inputMatches As Object, replaceMatches As Object, replaceMatch As Object
    Dim replaceNumber As Integer

    With inputRegexObj
        .Global = True
        .MultiLine = True
        .IgnoreCase = False
        .Pattern = matchPattern
    End With
    With outputRegexObj
        .Global = True
        .MultiLine = True
        .IgnoreCase = False
        .Pattern = "\$(\d+)"
    End With
    With outReplaceRegexObj
        .Global = True
        .MultiLine = True
        .IgnoreCase = False
    End With

    Set inputMatches = inputRegexObj.Execute(strInput)
    If inputMatches.Count = 0 Then
        regex = False
    Else
        Set replaceMatches = outputRegexObj.Execute(outputPattern)
        For Each replaceMatch In replaceMatches
            replaceNumber = replaceMatch.SubMatches(0)
            outReplaceRegexObj.Pattern = "\$" & replaceNumber

            If replaceNumber = 0 Then
                outputPattern = outReplaceRegexObj.Replace(outputPattern, inputMatches(0).Value)
            Else
                If replaceNumber > inputMatches(0).SubMatches.Count Then
                    'regex = "A to high $ tag found. Largest allowed is $" & inputMatches(0).SubMatches.Count & "."
                    regex = CVErr(xlErrValue)
                    Exit Function
                Else
                    outputPattern = outReplaceRegexObj.Replace(outputPattern, inputMatches(0).SubMatches(replaceNumber - 1))
                End If
            End If
        Next
        regex = outputPattern
    End If
End Function
