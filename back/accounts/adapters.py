from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        nickname = data.get("nickname")
        profile_image = data.get("profile_image")
        date_of_birth = data.get("date_of_birth")
        if nickname:
            user.nickname = nickname
        if profile_image:
            user.profile_image = profile_image
        if date_of_birth :
            user.date_of_birth = date_of_birth

        user.save()
        return user