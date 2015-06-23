# CustomDjangoForms

<code> fastFormFields.py </code> contains 2 Field classes and 1 Form class.

<ul>
<li><code>FastaTextField</code> - FormField class allowing users to input in an HTML text area.</li>
<li><code>FastaFileField</code> - FormField class for FASTA file upload.</li>
<li><code>FastaForm</code> - Form class containing the 2 fields above.</li>
</ul>

This form class is useful for bioinformaticians who would like to
validate the input/upload of FASTA sequences in forms.

<code> myFormFields.py </code> contains some extra field classes subclassing
from the <code>IntegerField</code>

<ul>
<li><code>PositiveIntegerField</code> </li>
<li><code>OptionalPositiveIntegerField</code> </li>
<li><code>OptionalPercentField</code> </li>

</ul>
